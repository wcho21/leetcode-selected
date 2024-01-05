// Accepted: 89ms (44.05%), 8.56MB (58.74%)

// dynamic programing

constexpr int MAX_S_LEN = 1001;

class Solution {
private:
    // DP table: [i][j]: i to j is palindrome
    bool palindrome[MAX_S_LEN][MAX_S_LEN];

public:
    string longestPalindrome(string s) {
        int n = s.size();

        int longestBeg = 0;
        int longestEnd = 0;

        // base case 1: length of 1
        for (int i = 0; i < n; ++i) {
            palindrome[i][i] = true;
        }

        // base case 2: length of 2
        for (int i = 0; i < n-1; ++i) {
            if (s[i] == s[i+1]) {
                palindrome[i][i+1] = true;
                longestBeg = i;
                longestEnd = i+1;
            }
        }

        // tabulation: length of n, from length of n-1
        for (int diff = 2; diff < n; ++diff) {
            for (int beg = 0; beg < n; ++beg) {
                int end = beg + diff;
                if (end >= n) {
                    continue;
                }

                if (!palindrome[beg+1][end-1]) {
                    continue;
                }
                if (s[beg] != s[end]) {
                    continue;
                }

                palindrome[beg][end] = true;
                longestBeg = beg;
                longestEnd = end;
            }
        }

        return s.substr(longestBeg, longestEnd-longestBeg+1);
    }
};
