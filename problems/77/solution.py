# Accepted: 640ms (92.96%), 64.65MB (76.64%)

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs: List[List[int]] = []

        def generateCombinations(i: int, k: int, collected: List[int]) -> None:
            if k == 0:
                combs.append(collected[:])
                return

            for j in range(i, n - (k-1) + 1):
                collected.append(j)
                generateCombinations(j+1, k-1, collected)
                collected.pop()

        generateCombinations(1, k, [])

        return combs
