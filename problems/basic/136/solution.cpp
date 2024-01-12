// Accepted: 7ms (98.24%), 17.10MB (99.19%)

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        return accumulate(nums.begin(), nums.end(), 0, [](const int a, const int b) {
            return a ^ b;
        });
    }
};
