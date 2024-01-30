# Accepted: 40ms (20.57%), 16.48MB (81.82%)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        digitToLetters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        combs = []

        def generateCombinations(i: int, collected: List[str]) -> None:
            if i >= len(digits):
                comb = "".join(collected)
                combs.append(comb)
                return

            digit = digits[i]
            letters = digitToLetters[digit]
            for l in letters:
                collected.append(l)
                generateCombinations(i+1, collected)
                collected.pop()

        generateCombinations(0, [])

        return combs
