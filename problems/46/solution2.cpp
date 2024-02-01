// Accepted: 3ms (54.69%), 10.80MB (5.18%)

class Solution {
    vector<vector<int>> permutations;
    void go(int i, vector<int>& nums) {
        if (i == nums.size()) {
            vector<int> permutation(nums.begin(), nums.end());
            permutations.push_back(permutation);
            return;
        }

        go(i+1, nums);
        for (int j = i+1; j < nums.size(); ++j) {
            swap(nums[i], nums[j]);
            go(i+1, nums);
            swap(nums[i], nums[j]);
        }
    }
public:
    vector<vector<int>> permute(vector<int>& nums) {
        go(0, nums);

        return permutations;
    }
};
