// Accepted: 73ms (41.82%), 53.65MB (17.13%)

function permute(nums: number[]): number[][] {
    const permutations: number[][] = [];
    const go = (k: number = nums.length) => {
        if (k === 1) {
            permutations.push(nums.slice(0));
            return;
        }

        go(k-1);
        for (let i = 0; i < k-1; ++i) {
            if (k % 2 == 0) {
                [nums[i], nums[k-1]] = [nums[k-1], nums[i]];
            } else {
                [nums[0], nums[k-1]] = [nums[k-1], nums[0]];
            }
            go(k-1);
        }
    };
    go();

    return permutations;
};
