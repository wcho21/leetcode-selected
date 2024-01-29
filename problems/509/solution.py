# Accepted: 37ms (70.98%), 16.47MB (67.67%)

class Solution:
    def fib(self, n: int) -> int:
        if n <= 0:
            return 0
        if n <= 2:
            return 1

        fibs = [0] * (n+1)
        fibs[1] = fibs[2] = 1

        for i in range(3, n+1):
            fibs[i] = fibs[i-1] + fibs[i-2]

        return fibs[n]
