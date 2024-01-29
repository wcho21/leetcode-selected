// Accepted: 0ms (100.00%), 9.18MB (34.70%)

class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() <= 2) {
            return *max_element(nums.begin(), nums.end());
        }

        vector<int> robbed(nums.size(), 0);
        robbed[0] = nums[0];
        robbed[1] = max(nums[0], nums[1]);

        for (int i = 2; i < nums.size(); ++i) {
            robbed[i] = max(robbed[i-1], robbed[i-2] + nums[i]);
        }

        return *max_element(robbed.begin(), robbed.end());
    }
};
