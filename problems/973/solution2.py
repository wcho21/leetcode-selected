# Accepted: 578ms (77.98%), 23.06MB (34.46%)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # get k smallest points in heap
        heap = []
        for p in points:
            d = p[0]*p[0] + p[1]*p[1]
            if len(heap) < k:
                heappush(heap, (-d, p)) # minus to use heap as max heap
            elif d < -heap[0][0]: # d < max distance in heap
                heapreplace(heap, (-d, p))

        kSmallest = nsmallest(k, heap)
        kSmallestPoints = list(map(lambda item: item[1], kSmallest))
        return kSmallestPoints
