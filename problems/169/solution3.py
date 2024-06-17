# Accepted: 179ms (21.93%), 17.98MB (64.06%)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore voting algorithm

        major = nums[0]
        count = 1

        for i in range(1, len(nums)):
            n = nums[i]

            if n == major:
                count += 1
            elif count > 0:
                count -= 1
            else:
                # assume new major
                major = n
                count = 1

        return major
