// Accepted: 465ms (61.87%), 121.22MB (98.44%)

function combine(n: number, k: number): number[][] {
    const combinations: number[][] = [];

    const generated: number[] = [];
    const go = (begin: number, k: number) => {
        if (k === 0) {
            combinations.push(generated.slice(0));
            return;
        }

        for (let i = begin; i < n-k+2; ++i) {
            generated.push(i);
            go(i+1, k-1);
            generated.pop();
        }
    };
    go(1, k);

    return combinations;
};
