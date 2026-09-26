#!/usr/bin/env python3
"""Generate one programming exercise, verify it actually runs, and commit it.

Nothing is committed unless the generated tests execute and pass, so the repo
only ever contains working code.
"""
from __future__ import annotations

import datetime as dt
import json
import pathlib
import random
import re
import shutil
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

# Arkheon is reached directly; the host exports a global proxy we must not use here.
DIRECT = urllib.request.build_opener(urllib.request.ProxyHandler({}))

TOPICS = [
    "a caching or memoization utility", "a rate limiter", "a retry policy with backoff",
    "a small parser for a text format", "a date or duration helper", "a diff or merge routine",
    "a priority queue or scheduler", "a string similarity metric", "a pagination helper",
    "a circular buffer", "a debounce or throttle mechanism", "a tiny expression evaluator",
    "a path or glob matcher", "a set of validation combinators", "a topological sort",
    "an LRU with TTL expiry", "a chunking or batching helper", "a deep merge of nested data",
    "a simple state machine", "a checksum or rolling hash",
]

PROMPT = """You are preparing one self-contained Python exercise.

Topic: {topic}

Return ONE JSON object and nothing else, with these keys:
  "slug"     kebab-case, 2-4 words, no dates
  "title"    a short human title
  "problem"  markdown: what to build, the signature, and 2-3 edge cases to respect
  "solution" complete Python 3 module source. Standard library only.
  "tests"    complete Python 3 test module using unittest. Standard library only.

Rules:
- The tests must import from the module named exactly `solution`.
- Cover the edge cases named in the problem, at least 4 test methods.
- No placeholders, no TODOs, no example usage blocks. The code must run as written.
- Return raw JSON. Do not wrap it in markdown fences.
"""


def ask(messages: list[dict], key: str, max_tokens: int = 4000) -> str:
    """Call Arkheon, retrying transient upstream failures."""
    body = json.dumps({"model": MODEL, "max_tokens": max_tokens, "messages": messages}).encode()
    last = None
    for attempt in range(4):
        req = urllib.request.Request(
            API, data=body,
            headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        )
        try:
            with DIRECT.open(req, timeout=180) as resp:
                return json.loads(resp.read())["choices"][0]["message"]["content"]
        except urllib.error.HTTPError as exc:
            last = f"HTTP {exc.code}"
            if exc.code < 500:
                raise
        except Exception as exc:
            last = f"{type(exc).__name__}: {exc}"
        time.sleep(3 * (attempt + 1))
    raise RuntimeError(f"Arkheon unavailable after 4 attempts ({last})")


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


def verify(task: dict) -> tuple[bool, str]:
    """Run the generated tests in a scratch directory."""
    with tempfile.TemporaryDirectory() as tmp:
        d = pathlib.Path(tmp)
        (d / "solution.py").write_text(task["solution"])
        (d / "test_solution.py").write_text(task["tests"])
        try:
            r = subprocess.run(
                [sys.executable, "-m", "unittest", "-v", "test_solution"],
                cwd=d, capture_output=True, text=True, timeout=120,
            )
            return r.returncode == 0, (r.stderr or r.stdout)[-2500:]
        except subprocess.TimeoutExpired:
            return False, "tests exceeded 120s (possible infinite loop)"


def git(*args: str, msg: str | None = None) -> None:
    cmd = ["git", "-C", str(ROOT)]
    if msg is not None:
        cmd += ["-c", f"user.name={AUTHOR[0]}", "-c", f"user.email={AUTHOR[1]}"]
    subprocess.run(cmd + list(args), check=True, capture_output=True, text=True)


def reindex() -> None:
    rows = []
    for p in sorted(TASKS.glob("*/*/problem.md"), reverse=True):
        title = next((l[2:].strip() for l in p.read_text().splitlines() if l.startswith("# ")), p.parent.name)
        rows.append(f"| {p.parent.name[:10]} | [{title}]({p.parent.relative_to(ROOT)}) |")
    (ROOT / "README.md").write_text(
        "# daily-build\n\n"
        "One self-contained programming exercise per day: the problem, an implementation,\n"
        "and tests. Generated nightly and committed only when the tests actually pass.\n\n"
        f"**{len(rows)} exercises.** Python 3, standard library only.\n\n"
        "| Date | Exercise |\n|---|---|\n" + "\n".join(rows) + "\n"
    )


def main() -> None:
    key = dict(
        l.split("=", 1) for l in pathlib.Path("/etc/arkheon.env").read_text().split() if "=" in l
    )["ARKHEON_API_KEY"]

    today = dt.date.today()
    if list(TASKS.glob(f"*/{today}-*")):
        print(f"already built for {today}")
        return

    done = {p.name.split("-", 3)[-1] for p in TASKS.glob("*/*") if p.is_dir()}
    topic = random.choice(TOPICS)

    messages = [{"role": "user", "content": PROMPT.format(topic=topic)}]
    task = parse(ask(messages, key))

    ok, log = verify(task)
    if not ok:
        # One correction pass: hand the failure back and let it fix its own code.
        messages += [
            {"role": "assistant", "content": json.dumps(task)},
            {"role": "user", "content":
                f"The tests failed:\n\n{log}\n\nReturn the corrected JSON object, same keys, same format."},
        ]
        task = parse(ask(messages, key))
        ok, log = verify(task)
        if not ok:
            print(f"discarded - tests still failing:\n{log[-600:]}")
            sys.exit(1)

    slug = re.sub(r"[^a-z0-9-]", "", task["slug"].lower())[:40] or "exercise"
    if slug in done:
        slug = f"{slug}-2"
    d = TASKS / str(today.year) / f"{today}-{slug}"
    d.mkdir(parents=True, exist_ok=True)

    (d / "problem.md").write_text(f"# {task['title']}\n\n{task['problem'].strip()}\n")
    git("add", str(d / "problem.md"))
    git("commit", "-q", "-m", f"problem: {task['title']}", msg=".")

    (d / "solution.py").write_text(task["solution"].rstrip() + "\n")
    git("add", str(d / "solution.py"))
    git("commit", "-q", "-m", f"implement {slug}", msg=".")

    (d / "test_solution.py").write_text(task["tests"].rstrip() + "\n")
    git("add", str(d / "test_solution.py"))
    git("commit", "-q", "-m", f"test {slug}", msg=".")

    reindex()
    git("add", "README.md")
    git("commit", "-q", "-m", f"index: {today}", msg=".")

    print(f"built {d.relative_to(ROOT)} - tests passed, 4 commits")


if __name__ == "__main__":
    main()
