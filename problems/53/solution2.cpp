// Accepted: 82ms (67.23%), 70.25MB (9.95%)

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int curSum = nums[0];
        int maxSum = curSum;

        for (int i = 1; i < nums.size(); ++i) {
            curSum = max(curSum+nums[i], nums[i]);
            maxSum = max(maxSum, curSum);
        }

        return maxSum;
    }
};
