export type Validator = (value: unknown) => boolean;

export const vString: Validator = (value) => typeof value === 'string';

export const vNumber: Validator = (value) =>
  typeof value === 'number' && Number.isFinite(value);

export const vBoolean: Validator = (value) => typeof value === 'boolean';

export const vOptional = (validator: Validator): Validator =>
  (value) => value === undefined || value === null || validator(value);

export const vArray = (validator: Validator): Validator =>
  (value) => Array.isArray(value) && value.every(validator);

export const vAll = (...validators: Validator[]): Validator =>
  (value) => validators.every((v) => v(value));

export const vAny = (...validators: Validator[]): Validator =>
  (value) => validators.some((v) => v(value));

export const vNot = (validator: Validator): Validator =>
  (value) => !validator(value);

export interface Schema {
  [key: string]: Validator;
}

export const vShape = (schema: Schema): Validator =>
  (value) => {
    if (typeof value !== 'object' || value === null || Array.isArray(value)) {
      return false;
    }
    const obj = value as Record<string, unknown>;
    return Object.entries(schema).every(([key, validator]) =>
      key in obj && validator(obj[key])
    );
  };
