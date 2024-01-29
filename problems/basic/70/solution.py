# Accepted: 27ms (94.94%), 16.68MB (72.85%)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

        numWays = [0] * (n+1)
        numWays[0] = numWays[1] = 1

        for i in range(2, n+1):
            numWays[i] = numWays[i-1] + numWays[i-2]

        return numWays[n]
