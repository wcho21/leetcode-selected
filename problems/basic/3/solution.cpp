// Accepted: 10ms (73.95%), 11.28MB (29.92%)

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int left = 0;
        int right = 0;
        unordered_map<char, int> lastOccur;
        int longest = 0;

        while (right < s.size()) {
            char ch = s[right];

            if (lastOccur.count(ch) == 0 || lastOccur[ch] < left) { // no repeating character contained
                longest = max(longest, right - left + 1);
            } else {
                left = lastOccur[ch]+1;
            }

            lastOccur[ch] = right;
            ++right;
        }

        return longest;
    }
};
