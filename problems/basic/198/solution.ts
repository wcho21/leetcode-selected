// Accepted: 57.ms (51.12%), 51.29MB (15.53%)

function rob(nums: number[]): number {
    if (nums.length <= 2) {
        return Math.max(...nums);
    }

    const robbed = Array(nums.length).fill(0);
    robbed[0] = nums[0];
    robbed[1] = Math.max(nums[0], nums[1]);

    for (let i = 2; i < nums.length; ++i) {
        robbed[i] = Math.max(robbed[i-1], robbed[i-2] + nums[i]);
    }

    return Math.max(...robbed);
};
