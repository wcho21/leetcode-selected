# Accepted: 195ms (31.35%), 18.04MB (63.86%)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums)

        while lower < upper:
            mid = lower + (upper-lower)//2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                upper = mid
            else:
                lower = mid+1

        return -1
