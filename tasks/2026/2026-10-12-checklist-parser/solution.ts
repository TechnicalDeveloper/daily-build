export interface Task {
  description: string;
  completed: boolean;
}

export function parseChecklist(input: string): Task[] {
  const lines = input.split('\n');
  const tasks: Task[] = [];

  const regex = /^\s*-\s+\[([ x])\]\s+(.*)$/;

  for (const line of lines) {
    const match = line.match(regex);
    if (match) {
      const completed = match[1] === 'x';
      const description = match[2].trimEnd();
      tasks.push({ description, completed });
    }
  }

  return tasks;
}
