// Accepted: 11ms (70.43%), 11.27MB (35.02%)

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> targetIndices;

        for (int i = 0; i < nums.size(); ++i) {
            int num = nums[i];

            if (targetIndices.count(num) != 0) {
                int targetIndex = targetIndices[num];
                return {i, targetIndex};
            }

            targetIndices[target-num] = i;
        }

        return { -1, -1 }; // failed
    }
};
