# Accepted: 170ms (92.60%), 21.60MB (24.96%)

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        mid = len(s) // 2
        end = len(s)-1

        for i in range(mid):
            s[i], s[end-i] = s[end-i], s[i]
