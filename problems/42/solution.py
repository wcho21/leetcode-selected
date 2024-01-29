# Accepted: 100ms (91.51%), 19.26MB (21.43%)

class Solution:
    def trap(self, height: List[int]) -> int:
        maxHeight = max(height)
        maxHeightIndex = height.index(maxHeight)

        water = 0

        # from left to the peak
        maxHeightSoFar = 0
        for i in range(maxHeightIndex):
            maxHeightSoFar = max(maxHeightSoFar, height[i])
            water += maxHeightSoFar - height[i]

        # from right to the peak
        maxHeightSoFar = 0
        for i in reversed(range(maxHeightIndex+1, len(height))):
            maxHeightSoFar = max(maxHeightSoFar, height[i])
            water += maxHeightSoFar - height[i]

        return water
