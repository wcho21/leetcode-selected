// Accepted: 0ms (100.00%), 7.50MB (5.72%)

class Solution {
public:
    int climbStairs(int n) {
        if (n <= 1) {
            return 1;
        }

        vector<int> numWays(n+1, 0);
        numWays[0] = numWays[1] = 1;

        for (int i = 2; i < n+1; ++i) {
            numWays[i] = numWays[i-1] + numWays[i-2];
        }

        return numWays[n];
    }
};
