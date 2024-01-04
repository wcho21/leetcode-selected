// Accepted: 78ms (77.54%), 50.20MB (34.54%)

/**
 Do not return anything, modify s in-place instead.
 */
function reverseString(s: string[]): void {
    const mid = Math.floor(s.length / 2);
    const end = s.length - 1;

    for (let i = 0; i < mid; ++i) {
        const temp = s[i];
        s[i] = s[end-i];
        s[end-i] = temp;
    }
};
