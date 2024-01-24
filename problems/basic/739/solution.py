# Accepted: 908ms (89.24%), 32.07 (37.93%)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        daysToWait = [0] * len(temperatures)
        stack: List[int] = []

        for day in range(len(temperatures)):
            while len(stack) > 0:
                pastDay = stack[-1]
                pastTemp = temperatures[pastDay]
                curTemp = temperatures[day]

                if pastTemp >= curTemp:
                    break

                daysToWait[pastDay] = day - pastDay
                stack.pop()

            stack.append(day)

        return daysToWait
