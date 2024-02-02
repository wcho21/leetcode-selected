# Accepted: 673ms (93.71%), 64.84MB (71.95%)

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations: List[List[int]] = []

        generated: List[int] = []
        def go(begin: int, k: int) -> None:
            if k == 0:
                combinations.append(generated[:])
                return

            for i in range(begin, n-k+2):
                generated.append(i)
                go(i+1, k-1)
                generated.pop()
        go(1, k)

        return combinations
