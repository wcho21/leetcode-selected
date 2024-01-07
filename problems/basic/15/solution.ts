// Accepted: 154ms (80.17%), 59.05MB (73.09%)

function threeSum(nums: number[]): number[][] {
    const triplets: number[][] = [];

    nums.sort((a, b) => a - b);

    let i = 0;
    while (i < nums.length-2) {
        // stop if the least number is positive, since the sum cannot be zero
        if (nums[i] > 0) {
            break;
        }

        const target = -nums[i];

        let j = i+1;
        let k = nums.length-1;

        // store the unique triplets whenever it finds two numbers that add up to the target sum
        while (j < k) {
            const sum = nums[j] + nums[k];
            if (sum < target) {
                j++;
                continue;
            }
            if (sum > target) {
                k--;
                continue;
            }

            // found
            triplets.push([nums[i], nums[j], nums[k]]);

            // skip the same values
            j++;
            while (j < k && nums[j-1] === nums[j]) {
                j++;
            }
            k--;
            while (j < k && nums[k] === nums[k+1]) {
                k--;
            }
        }

        // skip the same values
        i++;
        while (i < nums.length-2 && nums[i-1] === nums[i]) {
            i++;
        }
    }

    return triplets;
};
