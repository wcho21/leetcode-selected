# Accepted: 43ms (28.75%), 17.30MB (29.33%)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        digitToLetters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def getCombinations(i: int = 0) -> List[str]:
            if i == len(digits):
                return [""]

            digit = digits[i]
            letters = digitToLetters[digit]

            combinations = []
            for toCombine in getCombinations(i+1):
                for letter in letters:
                    combinations.append(letter+toCombine)

            return combinations

        return getCombinations()
