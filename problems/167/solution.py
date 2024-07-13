# Accepted: 101ms (77.69%), 17.74MB (6.56%)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lower = 0
        upper = len(numbers)

        while lower < upper-1:
            added = numbers[lower] + numbers[upper-1]
            if added == target:
                return [lower+1, upper]

            if added < target:
                lower += 1
            else:
                upper -= 1

        raise Exception("not found")
