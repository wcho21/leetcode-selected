# Accepted: 42ms (66.93%), 17.03MB (7.76%)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def searchPivot() -> None:
            lower = 0
            upper = len(nums)-1

            while lower < upper:
                mid = lower + (upper-lower)//2

                if nums[lower] < nums[upper]:
                    return lower

                if nums[mid] > nums[upper]:
                    lower = mid + 1
                else:
                    upper = mid

            return upper

        def binarySearch(pivot: int) -> None:
            lower = 0
            upper = len(nums)

            while lower < upper:
                mid = lower + (upper-lower)//2
                i = (mid + pivot) % len(nums)

                if nums[i] == target:
                    return i

                if nums[i] < target:
                    lower = mid+1
                else:
                    upper = mid

            return -1

        pivot = searchPivot()
        return binarySearch(pivot)
