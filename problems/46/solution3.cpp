// Accepted: 0ms (100.00%), 10.51MB (5.18%)

class Solution {
    vector<vector<int>> permutations;

    void go(int k, vector<int>& nums) {
        if (k == 1) {
            vector<int> permutation(nums.begin(), nums.end());
            permutations.push_back(permutation);
            return;
        }

        go(k-1, nums);
        for (int i = 0; i < k-1; ++i) {
            if (k % 2 == 0) {
                swap(nums[i], nums[k-1]);
            } else {
                swap(nums[0], nums[k-1]);
            }
            go(k-1, nums);
        }
    }
public:
    vector<vector<int>> permute(vector<int>& nums) {
        go(nums.size(), nums);

        return permutations;
    }
};
