# Accepted: 2479ms (35.88%), 25.38MB (5.48%)

# dynamic programming

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        # DP table: [i][j]: i to j is palindrome
        palindrome = [[False] * n for _ in range(n)]

        longestBeg = 0
        longestEnd = 0

        # base case 1: length of 1
        for i in range(n):
            palindrome[i][i] = True

        # base case 2: length of 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                palindrome[i][i+1] = True
                longestBeg = i
                longestEnd = i+1

        # tabulation: length of n, from length of n-1
        for diff in range(2, n):
            for beg in range(n):
                end = beg+diff
                if end >= n:
                    continue

                if not palindrome[beg+1][end-1]:
                    continue
                if s[beg] != s[end]:
                    continue

                palindrome[beg][end] = True
                longestBeg = beg
                longestEnd = end

        return s[longestBeg:longestEnd+1]
