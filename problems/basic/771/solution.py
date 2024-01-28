# Accepted: 34ms (78.47%), 16.48MB (65.36%)

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counts = [0] * (ord('z')+1)
        for stone in stones:
            counts[ord(stone)] += 1

        numJewels = sum(counts[ord(jewel)] for jewel in jewels)
        return numJewels
