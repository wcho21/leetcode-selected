// Accepted: 12ms (77.12%), 7.22MB (82.50%)

// sliding window

class Solution {
private:
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

    // scan palindrome with window, from left to right
    string scanLongestPalindrome(const string& s, int beg, int end) {
        int n = s.size();
        int longestBeg = -1;
        int longestEnd = -1;

        while (end < n) {
            if (!isPalindrome(s, beg, end)) {
                beg++;
                end++;
                continue;
            }

            longestBeg = beg;
            longestEnd = end;

            // move window to right, if end of boundary
            if (beg == 0 || end == n-1) {
                beg++;
                end++;
                continue;
            }

            // expand window
            beg--;
            end++;
        }

        // not found
        if (longestBeg == -1 || longestEnd == -1) {
            return "";
        }

        return s.substr(longestBeg, longestEnd-longestBeg+1);
    }
public:
    string longestPalindrome(string s) {
        string oddLength = scanLongestPalindrome(s, 0, 0);
        string evenLength = scanLongestPalindrome(s, 0, 1);

        return oddLength.size() > evenLength.size() ? oddLength : evenLength;
    }
};
