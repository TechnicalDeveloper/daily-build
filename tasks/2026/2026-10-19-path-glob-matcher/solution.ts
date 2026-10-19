export function match(pattern: string, path: string): boolean {
    const patternLen = pattern.length;
    const pathLen = path.length;

    function recurse(pi: number, si: number): boolean {
        if (pi === patternLen && si === pathLen) return true;
        if (pi === patternLen) return false;

        const pChar = pattern[pi];

        if (pChar === '*') {
            // Option 1: match zero characters (skip the *)
            if (recurse(pi + 1, si)) return true;
            // Option 2: match one character (if not '/') and stay on *
            if (si < pathLen && path[si] !== '/') {
                if (recurse(pi, si + 1)) return true;
            }
            return false;
        } else if (pChar === '?') {
            if (si < pathLen && path[si] !== '/') {
                return recurse(pi + 1, si + 1);
            }
            return false;
        } else {
            if (si < pathLen && path[si] === pChar) {
                return recurse(pi + 1, si + 1);
            }
            return false;
        }
    }

    return recurse(0, 0);
}
