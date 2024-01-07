// Accepted: 13ms (47.08%), 20.08 (77.79%)

class Solution {
public:
    int trap(vector<int>& height) {
        auto maxHeightIt = max_element(height.begin(), height.end());
        int maxHeightIndex = distance(height.begin(), maxHeightIt);

        int water = 0;

        // from left to the peak
        int maxHeightSoFar = 0;
        for (int i = 0; i < maxHeightIndex; ++i) {
            maxHeightSoFar = max(maxHeightSoFar, height[i]);
            water += maxHeightSoFar - height[i];
        }

        // from right to the peak
        maxHeightSoFar = 0;
        for (int i = height.size()-1; i > maxHeightIndex; --i) {
            maxHeightSoFar = max(maxHeightSoFar, height[i]);
            water += maxHeightSoFar - height[i];
        }

        return water;
    }
};
