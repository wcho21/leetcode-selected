# Accepted: 3371ms (29.86%), 17.34MB (31.95%)

# brute force

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

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longestBeg = 0
        longestEnd = 0

        for beg in range(n):
            for end in range(beg, n):
                if end - beg <= longestEnd - longestBeg:
                    continue
                if not self.isPalindrome(s, beg, end):
                    continue

                longestBeg = beg
                longestEnd = end

        return s[longestBeg:longestEnd+1]
