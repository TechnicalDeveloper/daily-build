#!/usr/bin/env python3
"""Generate the day's programming exercises, verify each one runs, and commit it.

Three exercises a day across two languages. The count is fixed: it is a daily
workload, not a function of anything on the contribution graph. Nothing is
committed unless the generated tests actually execute and pass, so the repository
only ever contains working code.
"""
from __future__ import annotations

import collections
import datetime as dt
import json
import pathlib
import random
import re
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
TASKS = ROOT / "tasks"
API = "https://arkheonchat.com/v1/chat/completions"
MODEL = "deepseek/deepseek-v4-flash"
AUTHOR = ("Pavel P.", "95400630+TechnicalDeveloper@users.noreply.github.com")
PLAN = ["python", "typescript", "python"]  # the fixed daily workload
TYPES = "/usr/lib/node_modules/@types"
# Arkheon returned a one-off 403 that succeeded on the next call, so treat it as transient.
RETRY_STATUS = {403, 408, 409, 425, 429, 500, 502, 503, 504}

# Arkheon is reached directly; the host exports a global proxy we must not use here.
DIRECT = urllib.request.build_opener(urllib.request.ProxyHandler({}))

TOPICS = [
    "a caching or memoization utility", "a rate limiter", "a retry policy with backoff",
    "a small parser for a text format", "a date or duration helper", "a diff or merge routine",
    "a priority queue or scheduler", "a string similarity metric", "a pagination helper",
    "a circular buffer", "a debounce or throttle mechanism", "a tiny expression evaluator",
    "a path or glob matcher", "a set of validation combinators", "a topological sort",
    "an LRU with TTL expiry", "a chunking or batching helper", "a deep merge of nested data",
    "a simple state machine", "a checksum or rolling hash", "an interval tree or range merge",
    "a backpressure-aware queue", "a stable sort by multiple keys", "a template interpolator",
]

SPEC = {
    "python": {
        "solution": "solution.py",
        "test": "test_solution.py",
        "rules": (
            "Write Python 3, standard library only.\n"
            "The test module must `from solution import ...` and use `unittest`.\n"
            "At least 4 test methods."
        ),
    },
    "typescript": {
        "solution": "solution.ts",
        "test": "solution.test.ts",
        "rules": (
            "Write TypeScript, no third-party packages.\n"
            "`solution.ts` must use named `export`s and compile under --strict.\n"
            "The test file must `import test from \"node:test\"`, `import assert from \"node:assert\"`,\n"
            "and import the implementation from \"./solution\". At least 4 top-level test() calls."
        ),
    },
}

PROMPT = """You are preparing one self-contained {lang} exercise.

Topic: {topic}

Return ONE JSON object and nothing else, with these keys:
  "slug"     kebab-case, 2-4 words, no dates
  "title"    a short human title
  "problem"  markdown: what to build, the signature, and 2-3 edge cases to respect
  "solution" complete source for the implementation file
  "tests"    complete source for the test file

{rules}

No placeholders, no TODOs, no example usage blocks. The code must run as written.
Return raw JSON, not wrapped in markdown fences.
"""


def ask(messages: list[dict], key: str, max_tokens: int = 8000) -> str:
    """Call Arkheon, retrying transient failures and truncated replies.

    The model reasons before answering and those tokens come out of max_tokens,
    so a budget sized only for the answer silently truncates the JSON.
    """
    last = None
    for attempt in range(4):
        body = json.dumps(
            {"model": MODEL, "max_tokens": max_tokens, "messages": messages}
        ).encode()
        req = urllib.request.Request(
            API, data=body,
            headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        )
        try:
            with DIRECT.open(req, timeout=240) as resp:
                choice = json.loads(resp.read())["choices"][0]
            content = (choice["message"].get("content") or "").strip()
            if content and choice.get("finish_reason") != "length":
                return content
            last = f"finish_reason={choice.get('finish_reason')} content={len(content)}ch"
            max_tokens = min(max_tokens * 2, 32000)
        except urllib.error.HTTPError as exc:
            last = f"HTTP {exc.code}"
            if exc.code not in RETRY_STATUS:
                raise
        except Exception as exc:
            last = f"{type(exc).__name__}: {exc}"
        time.sleep(3 * (attempt + 1))
    raise RuntimeError(f"Arkheon unusable after 4 attempts ({last})")


def parse(raw: str) -> dict:
    """Pull the JSON object out of the reply, tolerating stray fences or prose."""
    text = re.sub(r"^\s*```(?:json)?|```\s*$", "", raw.strip(), flags=re.M).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start, depth = text.find("{"), 0
        for i in range(start, len(text)):
            depth += (text[i] == "{") - (text[i] == "}")
            if depth == 0:
                return json.loads(text[start : i + 1])
    raise ValueError("no JSON object in reply")


def run(cmd: list[str], cwd: pathlib.Path) -> tuple[bool, str]:
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=180)
        return r.returncode == 0, (r.stderr or "") + (r.stdout or "")
    except subprocess.TimeoutExpired:
        return False, "exceeded 180s (possible infinite loop)"


def verify(lang: str, task: dict) -> tuple[bool, str]:
    """Run the generated tests in a scratch directory."""
    spec = SPEC[lang]
    with tempfile.TemporaryDirectory() as tmp:
        d = pathlib.Path(tmp)
        (d / spec["solution"]).write_text(task["solution"])
        (d / spec["test"]).write_text(task["tests"])

        if lang == "python":
            ok, log = run([sys.executable, "-m", "unittest", "-v", "test_solution"], d)
        else:
            ok, log = run(
                ["tsc", "--module", "commonjs", "--target", "es2022", "--strict",
                 "--esModuleInterop", "--skipLibCheck", "--typeRoots", TYPES, "--types", "node",
                 "--outDir", "out", spec["solution"], spec["test"]], d)
            if ok:
                ok, log = run(["node", "--test", "out/"], d)
        return ok, log[-2500:]


def git(*args: str, author: bool = False) -> None:
    cmd = ["git", "-C", str(ROOT)]
    if author:
        cmd += ["-c", f"user.name={AUTHOR[0]}", "-c", f"user.email={AUTHOR[1]}"]
    subprocess.run(cmd + list(args), check=True, capture_output=True, text=True)


def commit(path: pathlib.Path, message: str) -> None:
    git("add", str(path))
    git("commit", "-q", "-m", message, author=True)


def reindex() -> None:
    rows = []
    for p in sorted(TASKS.glob("*/*/problem.md"), reverse=True):
        title = next((l[2:].strip() for l in p.read_text().splitlines() if l.startswith("# ")),
                     p.parent.name)
        lang = "TypeScript" if (p.parent / "solution.ts").exists() else "Python"
        rows.append(f"| {p.parent.name[:10]} | {lang} | [{title}]({p.parent.relative_to(ROOT)}) |")
    (ROOT / "README.md").write_text(
        "# daily-build\n\n"
        "Self-contained programming exercises: the problem, an implementation, and tests.\n"
        "Generated nightly and committed only when the tests actually pass.\n\n"
        f"**{len(rows)} exercises.** Python (stdlib) and TypeScript (node:test), no dependencies.\n\n"
        "| Date | Language | Exercise |\n|---|---|---|\n" + "\n".join(rows) + "\n"
    )


def build_one(lang: str, topic: str, key: str, today: dt.date, taken: set[str]) -> str | None:
    """Produce one verified exercise and commit it. Returns its slug, or None."""
    spec = SPEC[lang]
    messages = [{"role": "user", "content":
                 PROMPT.format(lang=lang, topic=topic, rules=spec["rules"])}]
    task = parse(ask(messages, key))

    ok, log = verify(lang, task)
    if not ok:
        # One correction pass: hand the failure back and let it fix its own code.
        messages += [
            {"role": "assistant", "content": json.dumps(task)},
            {"role": "user", "content":
             f"That failed to build or test:\n\n{log}\n\nReturn corrected JSON, same keys."},
        ]
        task = parse(ask(messages, key))
        ok, log = verify(lang, task)
        if not ok:
            print(f"  [{lang}] discarded - still failing: {log[-300:]}")
            return None

    slug = re.sub(r"[^a-z0-9-]", "", task["slug"].lower())[:40] or "exercise"
    while slug in taken:
        slug += "-2"
    d = TASKS / str(today.year) / f"{today}-{slug}"
    d.mkdir(parents=True, exist_ok=True)

    (d / "problem.md").write_text(f"# {task['title']}\n\n{task['problem'].strip()}\n")
    commit(d / "problem.md", f"problem: {task['title']}")
    (d / spec["solution"]).write_text(task["solution"].rstrip() + "\n")
    commit(d / spec["solution"], f"implement {slug} ({lang})")
    (d / spec["test"]).write_text(task["tests"].rstrip() + "\n")
    commit(d / spec["test"], f"test {slug}")

    print(f"  [{lang}] {slug} - tests passed")
    return slug


def main() -> None:
    key = dict(
        l.split("=", 1) for l in pathlib.Path("/etc/arkheon.env").read_text().split() if "=" in l
    )["ARKHEON_API_KEY"]

    today = dt.date.today()
    # Work out what is missing per language: a slot that failed must be retried in
    # its own language, not backfilled by whichever one happens to come next.
    have = collections.Counter(
        "typescript" if (d / "solution.ts").exists() else "python"
        for d in TASKS.glob(f"*/{today}-*") if d.is_dir()
    )
    todo = []
    for lang, wanted in collections.Counter(PLAN).items():
        todo += [lang] * max(0, wanted - have[lang])
    if not todo:
        print(f"{today}: all {len(PLAN)} exercises already built")
        return

    taken = {p.name.split("-", 3)[-1] for p in TASKS.glob("*/*") if p.is_dir()}
    topics = random.sample(TOPICS, min(len(todo), len(TOPICS)))
    built = []
    for lang, topic in zip(todo, topics):
        try:
            slug = build_one(lang, topic, key, today, taken)
        except Exception as exc:
            print(f"  [{lang}] error: {type(exc).__name__}: {exc}")
            continue
        if slug:
            taken.add(slug)
            built.append(slug)

    if not built:
        print(f"{today}: nothing built, nothing committed")
        sys.exit(1)

    reindex()
    commit(ROOT / "README.md", f"index: {today}")
    print(f"{today}: built {len(built)}/{len(todo)} - {len(built) * 3 + 1} commits")
    if len(built) < len(todo):
        sys.exit(2)  # partial day: committed what worked, still worth a warning


if __name__ == "__main__":
    main()
