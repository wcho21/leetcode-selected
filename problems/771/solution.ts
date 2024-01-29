// Accepted: 46ms (97.55%), 51.50MB (14.48%)

function numJewelsInStones(jewels: string, stones: string): number {
    const counts = Array("z".charCodeAt(0)+1).fill(0);
    for (const stone of stones) {
        ++counts[stone.charCodeAt(0)];
    }

    const numJewels = Array.from(jewels)
        .map(jewel => counts[jewel.charCodeAt(0)])
        .reduce((a, b) => a + b);
    return numJewels;
};
