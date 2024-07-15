# Accepted: 92ms (34.71%), 17.34MB (6.27%)

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        for h, k in people:
            heappush(heap, (-h, k, h))

        queue = []
        while len(heap) > 0:
            _, k, h = heappop(heap)
            queue.insert(k, [h, k])

        return queue
