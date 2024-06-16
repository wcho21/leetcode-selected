# Accepted: 48ms (62.69%), 18.27MB (11.73%)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
