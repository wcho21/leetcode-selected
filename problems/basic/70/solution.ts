// Accepted: 57ms (48.16%), 49.55MB (8.18%)

function climbStairs(n: number): number {
    if (n <= 1) {
        return 1;
    }

    const numWays = Array(n+1).fill(0);
    numWays[0] = numWays[1] = 1;

    for (let i = 2; i < n+1; ++i) {
        numWays[i] = numWays[i-1] + numWays[i-2];
    }

    return numWays[n];
};
