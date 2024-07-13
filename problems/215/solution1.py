# Accepted: 549ms (12.63%), 29.85MB (48.93%)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            if len(heap) < k:
                heappush(heap, n)
            elif n > heap[0]:
                heapreplace(heap, n)

        return heap[0]
