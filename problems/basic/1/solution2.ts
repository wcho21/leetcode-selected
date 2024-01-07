// Accepted: 61ms (75.64%), 45.94MB (11.67%)

function twoSum(nums: number[], target: number): number[] {
    const targetIndices = new Map<number, number>();

    for (let i = 0; i < nums.length; ++i) {
        const num = nums[i];

        if (targetIndices.has(num)) {
            const targetIndex = targetIndices.get(num)!;
            return [targetIndex, i];
        }

        targetIndices.set(target-num, i);
    }

    return [-1, -1]; // failed
};
