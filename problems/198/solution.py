# Accepted: 30ms (92.18%), 16.61MB (37.34%)

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        robbed = [0] * len(nums)
        robbed[0] = nums[0]
        robbed[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            robbed[i] = max(robbed[i-1], robbed[i-2] + nums[i])

        return max(robbed)
