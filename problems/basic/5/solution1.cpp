// Accepted: 112ms (41.37%), 7.39MB (70.13%)

// brute force

class Solution {
    bool isPalindrome(const string& s, int beg, int end) {
        int left = beg;
        int right = end;

        while (left <= right) {
            if (s[left] != s[right]) {
                return false;
            }
            left++;
            right--;
        }

        return true;
    }

public:
    string longestPalindrome(string s) {
        int n = s.size();
        int longestBeg = 0;
        int longestEnd = 0;

        for (int beg = 0; beg < n; ++beg) {
            for (int end = beg; end < n; ++end) {
                if (end - beg <= longestEnd - longestBeg) {
                    continue;
                }
                if (!isPalindrome(s, beg, end)) {
                    continue;
                }

                longestBeg = beg;
                longestEnd = end;
            }
        }

        int longestLength = longestEnd-longestBeg+1;
        return s.substr(longestBeg, longestLength);
    }
};
