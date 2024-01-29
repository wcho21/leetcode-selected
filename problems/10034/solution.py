# Accepted: 35ms (100.00%), 17.35MB (100.00%)

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        suffix = int(s)

        if finish < suffix:
            return 0

        # determine upper and lower bounds of the interval to count
        divider = 10 ** len(s)
        lower, rem = divmod(start, divider)
        if rem > suffix:
            lower += 1
        upper, rem = divmod(finish, divider)
        if rem < suffix:
            upper -= 1

        # count the powerful numbers up to n
        def count(n):
            if n == -1:
                return 0
            if n == 0:
                return 1

            digits = [int(_) for _ in str(n)]
            numDigits = len(str(n))

            numCount = 0
            for i in range(numDigits):
                if digits[i] > limit:
                    numCount += (limit+1) ** (numDigits-i)
                    break

                numCount += digits[i] * ((limit+1) ** (numDigits-i-1))

                if i == numDigits-1:
                    numCount += 1

            return numCount

        return count(upper) - count(lower-1)
