# Accepted: 36ms (82.65%), 16.49MB (99.22%)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms: List[List[int]] = []
        visited: List[bool] = [False] * len(nums)

        def generatePermutations(i: int, collected: List[int]) -> None:
            if i >= len(nums):
                perms.append(collected[:])
                return

            for j in range(len(nums)):
                if visited[j]:
                    continue

                visited[j] = True
                collected.append(nums[j])

                generatePermutations(i+1, collected)

                visited[j] = False
                collected.pop()

        generatePermutations(0, [])

        return perms
