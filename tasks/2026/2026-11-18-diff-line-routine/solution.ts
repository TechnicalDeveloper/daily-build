export type DiffOp =
  | { type: "keep"; line: string }
  | { type: "delete"; line: string }
  | { type: "insert"; line: string };

export function diff(a: string[], b: string[]): DiffOp[] {
  const n = a.length;
  const m = b.length;

  // dp[i][j] = length of LCS of a[i..] and b[j..]
  const dp: number[][] = Array.from({ length: n + 1 }, () =>
    new Array<number>(m + 1).fill(0)
  );

  for (let i = n - 1; i >= 0; i--) {
    for (let j = m - 1; j >= 0; j--) {
      if (a[i] === b[j]) {
        dp[i][j] = dp[i + 1][j + 1] + 1;
      } else {
        dp[i][j] = Math.max(dp[i + 1][j], dp[i][j + 1]);
      }
    }
  }

  const ops: DiffOp[] = [];
  let i = 0;
  let j = 0;

  while (i < n && j < m) {
    if (a[i] === b[j]) {
      ops.push({ type: "keep", line: a[i] });
      i++;
      j++;
    } else if (dp[i + 1][j] >= dp[i][j + 1]) {
      ops.push({ type: "delete", line: a[i] });
      i++;
    } else {
      ops.push({ type: "insert", line: b[j] });
      j++;
    }
  }

  while (i < n) {
    ops.push({ type: "delete", line: a[i] });
    i++;
  }

  while (j < m) {
    ops.push({ type: "insert", line: b[j] });
    j++;
  }

  return ops;
}
