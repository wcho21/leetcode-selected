// Accepted: 3ms (59.20%), 7.28MB (5.42%)

class Solution {
public:
    int fib(int n) {
        if (n <= 0) {
            return 0;
        }
        if (n <= 2) {
            return 1;
        }

        vector<int> fibs(n+1, 0);
        fibs[1] = fibs[2] = 1;

        for (int i = 3; i <= n; ++i) {
            fibs[i] = fibs[i-1] + fibs[i-2];
        }

        return fibs[n];
    }
};
