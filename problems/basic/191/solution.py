# Accepted: 29ms (96.20%), 17.48MB (8.69%)

class Solution:
    def hammingWeight(self, n: int) -> int:
        dist = 0
        while n != 0:
            if n & 1:
                dist += 1
            n >>= 1
        return dist
