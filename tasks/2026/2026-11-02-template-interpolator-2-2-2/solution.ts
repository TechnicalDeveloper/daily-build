export function interpolate(template: string, values: Record<string, string | number | boolean | null | undefined>): string {
  return template.replace(/\{\{\s*(\w+)\s*\}\}/g, (match, key: string) => {
    const value = values[key];
    return value !== undefined && value !== null ? String(value) : '';
  });
}
