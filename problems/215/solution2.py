# Accepted: 467ms (60.17%), 29.57MB (81.51%)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums)-k

        def quickSelect(beg: int, end: int) -> int:
            while beg < end:
                i = partition(beg, end)
                if i == target:
                    return nums[i]

                if i > target:
                    end = i
                else:
                    beg = i+1

        def partition(beg: int, end: int) -> int:
            pivotIndex = random.randint(beg, end-1)
            nums[pivotIndex], nums[beg] = nums[beg], nums[pivotIndex]

            pivot = nums[beg]

            l = beg+1
            u = end

            while True:
                while l < end and nums[l] < pivot:
                    l += 1
                while nums[u-1] > pivot:
                    u -= 1

                if l < u:
                    nums[l], nums[u-1] = nums[u-1], nums[l]
                    l += 1
                    u -= 1
                else:
                    u -= 1
                    nums[beg], nums[u] = nums[u], nums[beg]
                    break

            return u

        return quickSelect(0, len(nums))
