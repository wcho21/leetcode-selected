// Accepted: 61m (31.83%), 43.30MB (48.54%)

function letterCombinations(digits: string): string[] {
    if (digits.length === 0) {
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
        "9": "wxyz",
    }

    const getCombinations = (i: number = 0): string[] => {
        if (i === digits.length) {
            return [""];
        }

        const digit = digits[i];
        const letters = digitToLetters[digit];

        const combinations: string[] = [];
        for (const toCombine of getCombinations(i+1)) {
            for (const letter of letters) {
                combinations.push(letter+toCombine);
            }
        }

        return combinations;
    }

    return getCombinations();
};
