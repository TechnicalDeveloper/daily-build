export type Result<T> = { success: true; value: T } | { success: false; errors: string[] };
export type Validator<T> = (value: unknown) => Result<T>;

export function vString(): Validator<string> {
  return (value) => {
    if (typeof value === "string") {
      return { success: true, value };
    }
    return { success: false, errors: ["expected a string"] };
  };
}

export function vNumber(): Validator<number> {
  return (value) => {
    if (typeof value === "number" && !Number.isNaN(value)) {
      return { success: true, value };
    }
    return { success: false, errors: ["expected a number"] };
  };
}

export function vBoolean(): Validator<boolean> {
  return (value) => {
    if (typeof value === "boolean") {
      return { success: true, value };
    }
    return { success: false, errors: ["expected a boolean"] };
  };
}

export function vArray<T>(item: Validator<T>): Validator<T[]> {
  return (value) => {
    if (!Array.isArray(value)) {
      return { success: false, errors: ["expected an array"] };
    }
    const errors: string[] = [];
    const result: T[] = [];
    for (let i = 0; i < value.length; i++) {
      const itemResult = item(value[i]);
      if (itemResult.success) {
        result.push(itemResult.value);
      } else {
        for (const err of itemResult.errors) {
          errors.push(`[${i}]: ${err}`);
        }
      }
    }
    if (errors.length) {
      return { success: false, errors };
    }
    return { success: true, value: result };
  };
}

type ObjectShape = Record<string, Validator<unknown>>;
export type InferShape<Shape extends ObjectShape> = {
  [K in keyof Shape]: Shape[K] extends Validator<infer T> ? T : never;
};

export function vObject<Shape extends ObjectShape>(shape: Shape): Validator<InferShape<Shape>> {
  return (value) => {
    if (typeof value !== "object" || value === null || Array.isArray(value)) {
      return { success: false, errors: ["expected an object"] };
    }
    const errors: string[] = [];
    const result: Record<string, unknown> = {};
    for (const key of Object.keys(shape)) {
      const v = shape[key];
      const fieldResult = v((value as Record<string, unknown>)[key]);
      if (fieldResult.success) {
        result[key] = fieldResult.value;
      } else {
        for (const err of fieldResult.errors) {
          errors.push(`${key}: ${err}`);
        }
      }
    }
    if (errors.length) {
      return { success: false, errors };
    }
    return { success: true, value: result as InferShape<Shape> };
  };
}

export function vOptional<T>(v: Validator<T>): Validator<T | undefined> {
  return (value) => {
    if (value === undefined) {
      return { success: true, value: undefined };
    }
    return v(value);
  };
}

export function vNullable<T>(v: Validator<T>): Validator<T | null> {
  return (value) => {
    if (value === null) {
      return { success: true, value: null };
    }
    return v(value);
  };
}

export function vAnd(...validators: Array<Validator<unknown>>): Validator<unknown> {
  return (value) => {
    const errors: string[] = [];
    for (const v of validators) {
      const result = v(value);
      if (!result.success) {
        errors.push(...result.errors);
      }
    }
    if (errors.length) {
      return { success: false, errors };
    }
    return { success: true, value };
  };
}

export function vOr(...validators: Array<Validator<unknown>>): Validator<unknown> {
  return (value) => {
    const allErrors: string[] = [];
    for (const v of validators) {
      const result = v(value);
      if (result.success) {
        return result;
      }
      allErrors.push(...result.errors);
    }
    return { success: false, errors: allErrors };
  };
}
