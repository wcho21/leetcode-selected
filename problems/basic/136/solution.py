# Accepted: 103ms (97.93%), 19.86MB (27.67%)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda a, b: a ^ b, nums)
