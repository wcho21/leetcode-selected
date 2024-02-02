// Accepted: 104ms (85.34%), 81.50MB (48.01%)

class Solution {
    vector<vector<int>> combinations;
    vector<int> generated;

    void go(int begin, int n, int k) {
        if (k == 0) {
            combinations.push_back(generated);
            return;
        }

        for (int i = begin; i < n-k+2; ++i) {
            generated.push_back(i);
            go(i+1, n, k-1);
            generated.pop_back();
        }
    }
public:
    vector<vector<int>> combine(int n, int k) {
        go(1, n, k);

        return combinations;
    }
};
