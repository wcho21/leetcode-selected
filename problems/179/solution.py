# Accepted: 47ms (21.52%), 16.57MB (21.02%)

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def isLess(num1: str, num2: str) -> bool:
            len1 = len(num1)
            len2 = len(num2)

            if len1 == len2:
                return int(num1) - int(num2)

            # imagine two strings are extended to the sum of their lengths
            # compare the extended ones
            maxLen = len1 + len2
            for i in range(maxLen):
                digit1 = num1[i % len1]
                digit2 = num2[i % len2]

                if digit1 != digit2:
                    return int(digit1) - int(digit2)

            return False

        # sort as strings, and join them
        strs = map(str, nums)
        sortedStrs = reversed(sorted(strs, key=cmp_to_key(isLess)))
        largest = "".join(sortedStrs)
        return str(int(largest))
