// Accepted: 70ms (5.71%), 51.27MB (64.07%)

function letterCombinations(digits: string): string[] {
    if (digits.length == 0) {
        return [];
    }

    const digitToLetters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxzy"
    };

    const combs: string[] = [];

    function generateCombinations(i: number, collected: string[]): void {
        if (i >= digits.length) {
            const comb = collected.join("");
            combs.push(comb);
            return;
        }

        const digit = digits[i];
        const letters = digitToLetters[digit];
        for (const l of letters) {
            collected.push(l);
            generateCombinations(i+1, collected);
            collected.pop();
        }
    }

    generateCombinations(0, []);

    return combs;
};
