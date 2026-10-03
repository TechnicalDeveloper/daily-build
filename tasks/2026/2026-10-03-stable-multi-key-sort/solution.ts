export type SortKey<T> = {
  key: keyof T;
  direction?: 'asc' | 'desc';
};

function compareValues<T>(a: T[keyof T], b: T[keyof T]): number {
  // treat null/undefined as less than any defined value
  if (a == null && b == null) return 0;
  if (a == null) return -1;
  if (b == null) return 1;

  // both are non-null/non-undefined at this point
  const aVal = a as Exclude<T[keyof T], null | undefined>;
  const bVal = b as Exclude<T[keyof T], null | undefined>;

  if (aVal < bVal) return -1;
  if (aVal > bVal) return 1;
  return 0;
}

export function stableSortByKeys<T>(
  items: T[],
  sortKeys: SortKey<T>[]
): T[] {
  // Return a copy to avoid mutating the original array
  const result = [...items];

  if (sortKeys.length === 0) {
    return result;
  }

  result.sort((a, b) => {
    for (const sortKey of sortKeys) {
      const direction = sortKey.direction === 'desc' ? -1 : 1;
      const cmp = compareValues(a[sortKey.key], b[sortKey.key]);
      if (cmp !== 0) {
        return cmp * direction;
      }
    }
    return 0; // all keys equal → stable (original order preserved by sort stability)
  });

  return result;
}
