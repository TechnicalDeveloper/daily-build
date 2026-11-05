function chunk<T>(array: T[], size: number): T[][] {
  if (size < 1) {
    throw new RangeError('size must be at least 1');
  }
  const result: T[][] = [];
  for (let i = 0; i < array.length; i += size) {
    result.push(array.slice(i, i + size));
  }
  return result;
}

export { chunk };
