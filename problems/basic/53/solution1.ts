// Accepted: 81ms (34.84%), 61.73MB (5.02%)

function maxSubArray(nums: number[]): number {
    const sums = Array(nums.length).fill(0);
    sums[0] = nums[0];

    for (let i = 1; i < sums.length; ++i) {
        sums[i] = Math.max(sums[i-1]+nums[i], nums[i]);
    }

    return Math.max(...sums);
};
