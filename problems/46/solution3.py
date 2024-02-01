# Accepted: 47ms (15.08%), 16.71MB (32.68%)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms: List[List[int]] = []

        def generatePermutations(i: int) -> None:
            if i == 0:
                perms.append(nums[:])
                return

            generatePermutations(i-1)
            for j in range(i):
                if i % 2 == 1:
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    nums[i], nums[0] = nums[0], nums[i]
                generatePermutations(i-1)

        generatePermutations(len(nums)-1)

        return perms
