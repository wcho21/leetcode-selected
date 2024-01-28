// Accepted: 68ms (70.15%), 56.28MB (6.30%)

function topKFrequent(nums: number[], k: number): number[] {
    const counts = new Map<number, number>();
    for (const num of nums) {
        counts.set(num, (counts.get(num) ?? 0)+1);
    }

    const countToNums = new Map<number, number[]>();
    for (const [num, count] of counts.entries()) {
        if (countToNums.has(count)) {
            countToNums.get(count)!.push(num);
        } else {
            countToNums.set(count, [num]);
        }
    }

    const tops: number[] = [];
    for (let count = nums.length; count > 0; --count) {
        if (!countToNums.has(count)) {
            continue;
        }

        for (const num of countToNums.get(count)!) {
            tops.push(num);
            k--;
        }

        if (k <= 0) {
            break;
        }
    }

    return tops;
};
