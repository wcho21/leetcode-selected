# Accepted: 34ms (81.50%), 17.18MB (34.65%)

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xored = x ^ y
        dist = 0
        while xored > 0:
            if (xored & 1) == 1:
                dist += 1
            xored >>= 1
        return dist
