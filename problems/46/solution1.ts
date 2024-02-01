// Accepted: 73ms (41.82%), 54.13MB (13.43%)

function permute(nums: number[]): number[][] {
    const permutations: number[][] = [];

    const generated: number[] = [];
    const visited = Array(nums.length).fill(false);

    const go = () => {
        if (generated.length === nums.length) {
            permutations.push(generated.slice(0));
            return;
        }

        for (let i = 0; i < nums.length; ++i) {
            if (visited[i]) {
                continue;
            }

            generated.push(nums[i]);
            visited[i] = true;

            go();

            generated.pop();
            visited[i] = false;
        }
    }
    go();

    return permutations;
};
