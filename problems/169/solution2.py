# Accepted: 326ms (5.18%), 18.82 (23.32%)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def getMajor(beg: int, end: int) -> int:
            if end - beg == 1:
                return nums[beg]

            mid = beg + (end - beg) // 2
            lower = getMajor(beg, mid)
            upper = getMajor(mid, end)

            numLower = sum(1 for i in range(beg, end) if nums[i] == lower)
            major = lower if numLower > (mid - beg) else upper
            return major

        return getMajor(0, len(nums))
