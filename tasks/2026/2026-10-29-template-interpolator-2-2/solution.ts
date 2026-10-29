export function interpolate(template: string, values: Record<string, string | number | boolean>): string {
  return template.replace(/\{\{(\w+)}}/g, (match, key) => {
    if (!(key in values)) {
      throw new Error(`Missing value for placeholder "${key}"`);
    }
    const value = values[key];
    return String(value);
  });
}
