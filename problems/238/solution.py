# Accepted: 171ms (87.83%), 25.64MB (12,79%)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProds = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            prefixProds[i] = prefixProds[i-1] * nums[i]

        suffixProds = [nums[-1]] * len(nums)
        for i in reversed(range(len(nums)-1)):
            suffixProds[i] = suffixProds[i+1] * nums[i]

        prods = []
        for i in range(len(nums)):
            prefix = prefixProds[i-1] if i > 0 else 1
            suffix = suffixProds[i+1] if i < len(nums)-1 else 1
            prods.append(prefix * suffix)

        return prods
