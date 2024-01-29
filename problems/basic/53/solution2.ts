// Accepted: 71ms (79.72%), 59.45MB (17.77%)

function maxSubArray(nums: number[]): number {
    let curSum = nums[0];
    let maxSum = curSum;

    for (let i = 1; i < nums.length; ++i) {
        curSum = Math.max(curSum+nums[i], nums[i]);
        maxSum = Math.max(maxSum, curSum);
    }

    return maxSum;
};
