// Accepted: 60ms (63.40%), 42.88MB (49.43%)

function hammingDistance(x: number, y: number): number {
    let xored = x ^ y;
    let dist = 0;
    while (xored > 0) {
        if ((xored & 1) === 1) {
            dist++;
        }
        xored >>= 1;
    }
    return dist;
};
