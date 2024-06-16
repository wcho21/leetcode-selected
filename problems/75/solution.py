# Accepted: 35ms (73.85%), 16.41MB (62.53%)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        m = 0
        u = len(nums)

        # [0, l): 0
        # [l, m): 1
        # [m, u): ?
        # [u, len): 2

        while m < u:
            num = nums[m]
            if num == 1:
                m += 1
            elif num == 2:
                u -= 1
                nums[m], nums[u] = nums[u], nums[m]
            else:
                nums[m], nums[l] = nums[l], nums[m]
                l += 1
                m += 1
