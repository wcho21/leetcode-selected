# Accepted: 45ms (96.20%), 16.71MB (57.29%)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        lastOccur = dict()
        longest = 0

        while right < len(s):
            ch = s[right]

            if ch not in lastOccur or lastOccur[ch] < left: # no repeating character contained
                longest = max(longest, right - left + 1)
            else:
                left = lastOccur[ch]+1

            lastOccur[ch] = right
            right += 1

        return longest
