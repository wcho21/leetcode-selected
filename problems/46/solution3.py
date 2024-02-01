# Accepted: 38ms (83.13%), 16.90MB (54.90%)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations: List[List[int]] = []
        def go(k: int = len(nums)) -> None:
            if k == 1:
                permutations.append(nums[:])
                return

            go(k-1)

            for i in range(k-1):
                if k % 2 == 0:
                    nums[i], nums[k-1] = nums[k-1], nums[i]
                else:
                    nums[0], nums[k-1] = nums[k-1], nums[0]

                go(k-1)
        go()

        return permutations
