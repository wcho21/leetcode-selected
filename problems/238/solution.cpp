// Accepted: 19ms (59.92%), 25.46MB (25.38%)

constexpr int MAX_NUMS_LEN = int(1e5+1);

class Solution {
    int prefixProds[MAX_NUMS_LEN];
    int suffixProds[MAX_NUMS_LEN];
    int prods[MAX_NUMS_LEN];
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        prefixProds[0] = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            prefixProds[i] = prefixProds[i-1] * nums[i];
        }

        suffixProds[nums.size()-1] = nums[nums.size()-1];
        for (int i = nums.size()-2; i > 0; --i) {
            suffixProds[i] = suffixProds[i+1] * nums[i];
        }

        for (int i = 0; i < nums.size(); ++i) {
            int prefix = i > 0 ? prefixProds[i-1] : 1;
            int suffix = i < nums.size()-1 ? suffixProds[i+1] : 1;
            prods[i] = prefix * suffix;
        }

        vector<int> prodsVec(prods, prods+nums.size());
        return prodsVec;
    }
};
