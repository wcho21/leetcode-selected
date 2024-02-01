# Accepted: 41ms (53.25%), 16.94MB (9.46%)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms: List[List[int]] = []

        def generatePermutations(i: int) -> None:
            if i == 0:
                perms.append(nums[:])
                return

            generatePermutations(i-1)
            for j in range(i):
                nums[i], nums[j] = nums[j], nums[i]
                generatePermutations(i-1)
                nums[i], nums[j] = nums[j], nums[i]

        generatePermutations(len(nums)-1)

        return perms
