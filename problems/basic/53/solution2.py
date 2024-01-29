# Accepted: 570ms (50.91%), 30.67MB (71.51%)

class Solution:
    def maxSubArray(self, nums):
        curSum = nums[0]
        maxSum = curSum

        for i in range(1, len(nums)):
            curSum = max(nums[i], curSum + nums[i])
            maxSum = max(maxSum, curSum)

        return maxSum

