// Accepted: 4ms (31.04%), 9.8MB (33.64%)

class Solution {
    void swap(vector<int>& nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

public:
    // Dijkstra's three-way partitioning algorithm
    void sortColors(vector<int>& nums) {
        int len = nums.size();
        int l = 0;
        int m = 0;
        int u = nums.size();

        // [0, l): 0
        // [l, m): 1
        // [m, u): ?
        // [u, len): 2

        while (m < u) {
            if (nums[m] == 1) {
                ++m;
            } else if (nums[m] == 2) {
                --u;
                swap(nums, m, u);
            } else { // nums[m] == 0
                swap(nums, l, m);
                ++l;
                ++m;
            }
        }
    }
};
