// Accepted: 64ms (50.29%), 49.78MB (10.58%)

function fib(n: number): number {
    if (n <= 0) {
        return 0;
    }
    if (n <= 2) {
        return 1;
    }

    const fibs = Array(n+1).fill(0);
    fibs[1] = fibs[2] = 1;

    for (let i = 3; i <= n; ++i) {
        fibs[i] = fibs[i-1] + fibs[i-2];
    }

    return fibs[n];
};
