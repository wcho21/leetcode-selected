# Accepted: 54ms (95.12%), 18.83MB (7.05%)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetIndices: Dict[int, int] = dict()

        for i, num in enumerate(nums):
            if num in targetIndices:
                targetIndex = targetIndices[num]
                return [targetIndex, i]

            targetIndices[target-num] = i

        return [-1, -1] # failed
