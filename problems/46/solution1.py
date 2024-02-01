# Accepted: 54ms (13.10%), 16.70MB (72.92%)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations: List[List[int]] = []

        generated: List[int] = []
        visited = [False] * len(nums)

        def go() -> None:
            if len(generated) == len(nums):
                permutations.append(generated[:])
                return

            for i in range(len(nums)):
                if visited[i]:
                    continue

                generated.append(nums[i])
                visited[i] = True

                go()

                generated.pop()
                visited[i] = False
        go()

        return permutations
