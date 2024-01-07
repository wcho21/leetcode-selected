// Accepted: 74ms (98.81%), 24.26MB (97.83%)

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> triplets;

        sort(nums.begin(), nums.end());

        int i = 0;
        while (i < nums.size()-2) {
            // stop if the least number is positive, since the sum cannot be zero
            if (nums[i] > 0) {
                break;
            }

            int target = -nums[i];

            int j = i+1;
            int k = nums.size()-1;

            // store the unique triplets whenever it finds two numbers that add up to the target sum
            while (j < k) {
                int sum = nums[j] + nums[k];
                if (sum < target) {
                    j++;
                    continue;
                }
                if (sum > target) {
                    k--;
                    continue;
                }

                // found
                triplets.push_back({nums[i], nums[j], nums[k]});

                // skip the same values
                j++;
                while (j < k && nums[j-1] == nums[j]) {
                    j++;
                }
                k--;
                while (j < k && nums[k] == nums[k+1]) {
                    k--;
                }
            }

            // skip the same values
            i++;
            while (i < nums.size()-2 && nums[i-1] == nums[i]) {
                i++;
            }
        }

        return triplets;
    }
};
