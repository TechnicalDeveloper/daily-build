# Validation Combinators

Build a small library of validation combinators. Each combinator is a function that returns a validator. A validator is a function that takes `unknown` and returns a discriminated union `Result<T>`:

```ts
type Result<T> = { success: true; value: T } | { success: false; errors: string[] };
type Validator<T> = (value: unknown) => Result<T>;
```

Implement the following combinators:

- `vString()`: `Validator<string>`
- `vNumber()`: `Validator<number>` (must reject `NaN`)
- `vBoolean()`: `Validator<boolean>`
- `vArray(item: Validator<T>)`: `Validator<T[]>`
- `vObject(shape: { [key: string]: Validator<unknown> })`: `Validator<...>` (infer output type)
- `vOptional(v)`: `Validator<T | undefined>` (allows `undefined`, but if value is present, run `v`)
- `vNullable(v)`: `Validator<T | null>` (allows `null`, but if value is present, run `v`)
- `vAnd(...validators)`: `Validator<unknown>` (all must pass, errors are concatenated)
- `vOr(...validators)`: `Validator<unknown>` (first success wins, errors from all are collected if all fail)

Edge cases:
- `vNumber` must reject `NaN` and non-number values.
- `vObject` must treat `null` and arrays as invalid objects.
- `vArray` errors should contain element indices, e.g., `"[2]: expected a string"`.
- `vObject` errors should contain the key, e.g., `age: expected a number`.
- `vOptional` does NOT allow `null`; use `vNullable` for that.
- `vAnd` and `vOr` accept any number of validators (including none, but for practical purposes at least one should be provided).

All code must be TypeScript, use named exports, and compile under `--strict`.
