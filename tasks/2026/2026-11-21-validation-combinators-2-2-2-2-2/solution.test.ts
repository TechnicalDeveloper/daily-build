import test from 'node:test';
import assert from 'node:assert';
import {
  vString,
  vNumber,
  vBoolean,
  vOptional,
  vArray,
  vAll,
  vAny,
  vNot,
  vShape,
} from './solution';

test('base validators', () => {
  assert.ok(vString('hello'));
  assert.ok(!vString(123));
  assert.ok(vNumber(42));
  assert.ok(!vNumber(Number.NaN));
  assert.ok(!vNumber(Infinity));
  assert.ok(vBoolean(true));
  assert.ok(!vBoolean('true'));
});

test('vOptional', () => {
  const maybeString = vOptional(vString);
  assert.ok(maybeString('abc'));
  assert.ok(maybeString(undefined));
  assert.ok(maybeString(null));
  assert.ok(!maybeString(123));
});

test('vArray', () => {
  const numbers = vArray(vNumber);
  assert.ok(numbers([1, 2, 3]));
  assert.ok(!numbers([1, 'two', 3]));
  assert.ok(!numbers('not array'));
  assert.ok(numbers([]));
});

test('vAll and vAny', () => {
  const stringAndNumber = vAll(vString, vNumber);
  assert.ok(!stringAndNumber('123'));
  assert.ok(!stringAndNumber(123));
  const stringOrNumber = vAny(vString, vNumber);
  assert.ok(stringOrNumber('abc'));
  assert.ok(stringOrNumber(123));
  assert.ok(!stringOrNumber(true));
});

test('vNot', () => {
  const notString = vNot(vString);
  assert.ok(notString(42));
  assert.ok(!notString('hello'));
});

test('vShape', () => {
  const point = vShape({ x: vNumber, y: vNumber });
  assert.ok(point({ x: 1, y: 2 }));
  assert.ok(!point({ x: 1 }));
  assert.ok(!point({ x: 'a', y: 2 }));
  assert.ok(!point(null));
  assert.ok(!point([1, 2]));

  const complex = vShape({
    name: vString,
    age: vOptional(vNumber),
    tags: vArray(vString),
  });
  assert.ok(complex({ name: 'Alice', age: undefined, tags: ['a'] }));
  assert.ok(complex({ name: 'Bob', age: 30, tags: [] }));
  assert.ok(!complex({ name: 42, tags: ['x'] }));
  assert.ok(!complex({ name: 'Alice', tags: ['x'] }));
});
