# Accepted: 349ms (86.80%), 17.32MB (31.95%)

# sliding window

class Solution:
    def isPalindrome(self, s: str, beg: int, end: int) -> bool:
        left = beg
        right = end

        while left <= right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True

    def scanLongestPalindrome(self, s: str, beg: int, end: int) -> string:
        n = len(s)
        longestBeg = -1
        longestEnd = -1

        # scan palindrome with window, from left to right
        while end < n:
            if not self.isPalindrome(s, beg, end):
                beg += 1
                end += 1
                continue

            longestBeg = beg
            longestEnd = end

            # move window to right, if end of bounary
            if beg == 0 or end == n-1:
                beg += 1
                end += 1
                continue

            # expand window
            beg -= 1
            end += 1

        # not found
        if longestBeg == -1 or longestEnd == -1:
            return ""

        return s[longestBeg:longestEnd+1]

    def longestPalindrome(self, s: str) -> str:
        oddLength = self.scanLongestPalindrome(s, 0, 0)
        evenLength = self.scanLongestPalindrome(s, 0, 1)

        return oddLength if len(oddLength) > len(evenLength) else evenLength
