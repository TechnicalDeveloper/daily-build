# Validation Combinators

Build a small library of validation combinators. A validator is a function `(value: unknown) => boolean`. Implement the following named exports in `solution.ts`:

- `vString`, `vNumber`, `vBoolean` – base validators for primitive types. `vNumber` should accept only finite numbers.
- `vOptional(validator)` – succeeds if the value is `undefined`, `null`, or passes the inner validator.
- `vArray(validator)` – succeeds if the value is an array and every element passes the inner validator.
- `vAll(...validators)` – succeeds if all validators succeed (logical AND).
- `vAny(...validators)` – succeeds if at least one validator succeeds (logical OR).
- `vNot(validator)` – succeeds if the inner validator fails (logical NOT).
- `vShape(schema)` – `schema` is an object where each key corresponds to a validator. Succeeds if the value is a plain object (not an array, not null) and for every key in `schema`, that key exists in the value and its value passes the corresponding validator. Extra keys in the value are allowed.

Edge cases to respect:
- `vOptional` must treat both `undefined` and `null` as valid and should not pass them to the inner validator.
- `vArray` must reject non‑array values (e.g., objects, strings, numbers).
- `vShape` must reject arrays and `null` even if they contain matching keys, and must fail when a required key is missing.
- All combinators must work with any of the base validators and can be nested freely.
