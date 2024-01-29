# Accepted: 1720ms (32.61%), 18.14MB (24.55%)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return [-1, -1] # failed
