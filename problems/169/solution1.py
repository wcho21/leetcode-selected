# Accepted: 130ms (89.29%), 18.00MB (58.23%)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return list(sorted(nums))[len(nums) // 2]
