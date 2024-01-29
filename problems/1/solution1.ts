// Accepted: 88ms (40.49%), 43.60MB (93.75%)

function twoSum(nums: number[], target: number): number[] {
    for (let i = 0; i < nums.length-1; ++i) {
        for (let j = i+1; j < nums.length; ++j) {
            if (nums[i] + nums[j] === target) {
                return [i, j];
            }
        }
    }

    return [-1, -1]; // failed
};
