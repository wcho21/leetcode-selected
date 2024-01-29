// Accepted: 108ms (7.33%), 60.97MB (5.32%)

function maxSubArray(nums: number[]): number {
    const go = (left: number = 0, right: number = nums.length): number => { // right is exclusive end
        const diff = right - left;
        if (diff === 1) {
            return nums[left];
        }
        if (diff <= 0) {
            throw new Error();
        }

        // get left and right max to get crossed max
        const mid = left + Math.floor(diff / 2);

        let leftSum = nums[mid-1];
        let leftMax = leftSum;
        for (let i = mid-2; i >= left; --i) {
            leftSum += nums[i];
            leftMax = Math.max(leftMax, leftSum);
        }

        let rightSum = nums[mid];
        let rightMax = rightSum;
        for (let i = mid+1; i < right; ++i) {
            rightSum += nums[i];
            rightMax = Math.max(rightMax, rightSum);
        }

        const crossedMax = leftMax + rightMax;

        return Math.max(go(left, mid), go(mid, right), crossedMax);
    };

    return go();
};
