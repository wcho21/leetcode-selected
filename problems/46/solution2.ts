// Accepted: 73ms (41.82%), 54.49MB (10.80%)

function permute(nums: number[]): number[][] {
    const permutations: number[][] = [];

    const go = (i: number = 0) => {
        if (i === nums.length) {
            permutations.push(nums.slice(0));
            return;
        }

        go(i+1);
        for (let j = i+1; j < nums.length; ++j) {
            [nums[i], nums[j]] = [nums[j], nums[i]];
            go(i+1);
            [nums[i], nums[j]] = [nums[j], nums[i]];
        }
    };
    go();

    return permutations;
};
