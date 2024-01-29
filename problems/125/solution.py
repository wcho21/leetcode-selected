# Accepted: 46ms (77.49%), 18.79 MB (16.11%)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = "".join(filter(lambda x: x.isalnum(), s.lower()))

        return filtered == filtered[::-1]
