// Accepted: 59ms (66.61%), 44.18MB (90.86%)

function hammingWeight(n: number): number {
    let dist = 0;
    while (n !== 0) {
        if ((n & 1) == 1) {
            dist++;
        }
        n >>>= 1;
        // note that the >> operator is signed shift (e.g., -1 >> 1 === -1)
    }
    return dist;
};
