# Accepted: 1535ms (5.01%), 45.70MB (7.93%)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def go(left: int = 0, right: int = len(nums)) -> int: # right is exclusive end
            diff = right - left
            if diff == 1:
                return nums[left]
            if diff <= 0:
                raise Exception

            # get left and right max to get crossed max
            mid = left + diff // 2

            leftSum = nums[mid-1]
            leftMax = nums[mid-1]
            for i in reversed(range(left, mid-1)):
                leftSum += nums[i]
                leftMax = max(leftMax, leftSum)

            rightSum = nums[mid]
            rightMax = nums[mid]
            for i in range(mid+1, right):
                rightSum += nums[i]
                rightMax = max(rightMax, rightSum)

            crossedMax = leftMax + rightMax

            return max(go(left, mid), go(mid, right), crossedMax)

        return go(0, len(nums))
