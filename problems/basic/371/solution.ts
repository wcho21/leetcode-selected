// Accepted: 49ms (86.54%), 42.72MB (45.19%)

function getSum(a: number, b: number): number {
    while (true) {
        const carry = (a & b) << 1;
        const added = a ^ b;

        if (carry === 0) {
            return added;
        }

        a = carry;
        b = added;
    }
};
