export function deepMerge(target: any, source: any): any {
  const isPlainObject = (val: any): val is Record<string, any> =>
    typeof val === 'object' && val !== null && !Array.isArray(val);

  const result: any = { ...target };

  for (const key of Object.keys(source)) {
    if (source[key] === undefined) continue;
    if (isPlainObject(result[key]) && isPlainObject(source[key])) {
      result[key] = deepMerge(result[key], source[key]);
    } else {
      result[key] = source[key];
    }
  }

  return result;
}
