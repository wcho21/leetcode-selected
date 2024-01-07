# Accepted: 604ms (100.00%), 31.95MB (25.00%)

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # xor all
        xor = nums[0]
        for i in range(1, len(nums)):
            xor ^= nums[i]

        # count the number of different digits in binary
        count = 0
        while xor > 0 or k > 0:
            one1 = xor & 1
            one2 = k & 1

            if one1 != one2:
                count += 1

            xor >>= 1
            k >>= 1

        return count
