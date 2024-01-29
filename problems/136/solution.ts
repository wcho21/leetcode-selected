// Accepted: 54ms (90.78%), 45.70MB (65.42%)

function singleNumber(nums: number[]): number {
    return nums.reduce((a, b) => a ^ b);
};
