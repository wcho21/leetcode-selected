# Accepted: 548ms (97.13%), 22.68MB (82.98%)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sortedPoints = list(sorted(points, key=lambda p: p[0]*p[0] + p[1]*p[1]))
        return sortedPoints[:k]
