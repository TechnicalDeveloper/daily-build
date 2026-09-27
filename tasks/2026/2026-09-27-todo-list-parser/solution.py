def parse_todo(text: str) -> list[dict]:
    tasks = []
    for line in text.splitlines():
        stripped_line = line.strip()
        if not stripped_line:
            continue
        # Check for incomplete task
        if stripped_line.startswith("- [ ] "):
            description = stripped_line[6:].strip()
            tasks.append({"completed": False, "description": description})
        # Check for completed task (case-insensitive 'x')
        elif stripped_line[:6].lower() == "- [x] ":
            description = stripped_line[6:].strip()
            tasks.append({"completed": True, "description": description})
        # else ignore line
    return tasks
