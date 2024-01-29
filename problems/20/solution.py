# Accepted: 34ms (83.79%), 17.45MB (6.15%)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in "({[":
                stack.append(c)
                continue

            # return false if unmatched closing parenthesis
            if len(stack) == 0:
                return False

            pop = stack.pop()

            if c == ")" and pop != "(":
                return False
            if c == "}" and pop != "{":
                return False
            if c == "]" and pop != "[":
                return False

        # return false if any unmatched opening parenthesis
        if len(stack) != 0:
            return False

        return True
