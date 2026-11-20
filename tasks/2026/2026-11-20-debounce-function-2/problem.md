# Implement a Debounce Function

Implement a debounce function that delays the invocation of a callback until after `delay` milliseconds have elapsed since the last call.

**Signature**
```typescript
function debounce<T extends (...args: any[]) => void>(func: T, delay: number): (...args: Parameters<T>) => void;
```

**Edge Cases**
- Multiple calls within the delay window should reset the timer; only the last call's arguments should be used.
- The callback must not be invoked before the delay has passed.
- The returned function should work with any number of arguments.
