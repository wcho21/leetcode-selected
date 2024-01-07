// Accepted: 99ms (82.50%), 49.98MB (10.83%)

function arrayPairSum(nums: number[]): number {
    return nums.sort((a, b) => a - b).filter((_, i) => i % 2 === 0).reduce((a, b) => a + b);
};
