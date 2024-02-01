// Accepted: 0ms (100.00%), 9.99MB (10.68%)

class Solution {
    static constexpr int MAX_LEN = 6;

    vector<vector<int>> permutations;
    vector<int> generated;
    int visited[MAX_LEN+1];

    void go(vector<int>& nums) {
        if (generated.size() == nums.size()) {
            vector<int> permutation(generated.begin(), generated.end());
            permutations.push_back(permutation);
            return;
        }

        for (int i = 0; i < nums.size(); ++i) {
            if (visited[i]) {
                continue;
            }

            generated.push_back(nums[i]);
            visited[i] = true;

            go(nums);

            generated.pop_back();
            visited[i] = false;
        }
    }
public:
    vector<vector<int>> permute(vector<int>& nums) {
        go(nums);

        return permutations;
    }
};
