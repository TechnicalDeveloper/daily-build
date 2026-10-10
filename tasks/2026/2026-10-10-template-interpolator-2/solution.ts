export function interpolate(template: string, data: Record<string, string | number | boolean>): string {
  return template.replace(/\{\{(\w+)\}\}/g, (match, key) => {
    if (!(key in data)) {
      throw new Error(`Missing key: ${key}`);
    }
    const value = data[key];
    return String(value);
  });
}
