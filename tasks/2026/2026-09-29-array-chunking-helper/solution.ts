export function chunk<T>(array: T[], size: number): T[][] {
  if (size <= 0) {
    throw new Error('Size must be a positive integer');
  }

  const chunks: T[][] = [];
  for (let i = 0; i < array.length; i += size) {
    chunks.push(array.slice(i, i + size));
  }
  return chunks;
}
