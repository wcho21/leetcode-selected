# Accepted: 33ms (100.00%), 17.33MB (40.00%)

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        numsSet = set(nums)

        # get the sum for the sequential prefix
        seqEnd = 0
        for i in range(1, len(nums)):
            if nums[i-1]+1 == nums[i]:
                seqEnd = i
            else:
                break

        seqSum = sum(nums[:seqEnd+1])

        # return the smallest missing integer greater than or equal to the sum
        while True:
            if seqSum not in numsSet:
                return seqSum

            seqSum += 1
