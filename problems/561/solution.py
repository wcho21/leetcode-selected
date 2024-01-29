# Accepted: 213ms (97.10%), 20.80MB (5.11%)

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
