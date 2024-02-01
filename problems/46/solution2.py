# Accepted: 43ms (57.12%), 16.71MB (62.05%)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations: List[List[num]] = []

        def go(i: int = 0):
            if i == len(nums):
                permutations.append(nums[:])
                return

            go(i+1)
            for j in range(i+1, len(nums)):
                nums[j], nums[i] = nums[i], nums[j]
                go(i+1)
                nums[j], nums[i] = nums[i], nums[j]
        go()

        return permutations
