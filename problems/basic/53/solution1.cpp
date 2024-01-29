// Accepted: 71ms (94.53%), 72.89MB (6.32%)

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        vector<int> sums(nums.size(), 0);
        sums[0] = nums[0];

        for (int i = 1; i < nums.size(); ++i) {
            sums[i] = max(sums[i-1]+nums[i], nums[i]);
        }

        return *max_element(sums.begin(), sums.end());
    }
};
