# Accepted: 121ms (67.39%), 20.50MB (82.44%)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sortedIntervals = list(sorted(intervals))

        # if overlapped, update the last interval Y; otherwise, push new interval into stack
        stack = []
        for interval in sortedIntervals:
            if len(stack) == 0:
                stack.append(interval)
                continue

            if stack[-1][1] < interval[0]: # last interval Y < current interval X
                stack.append(interval)
                continue

            stack[-1][1] = max(stack[-1][1], interval[1]) # update last interval Y

        return stack
