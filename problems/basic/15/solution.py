# Accepted: 444ms (99.48%), 21.62MB (14.24%)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []

        nums.sort()

        i = 0
        while i < len(nums)-2:
            # stop if the least number is positive, since the sum cannot be zero
            if nums[i] > 0:
                break

            target = -nums[i]

            j = i+1
            k = len(nums)-1

            # store the unique triplets whenever it finds two numbers that add up to the target sum
            while j < k:
                twoSum = nums[j] + nums[k]
                if twoSum < target:
                    j += 1
                    continue
                if twoSum > target:
                    k -= 1
                    continue

                # found
                triplets.append([nums[i], nums[j], nums[k]])

                # skip the same values
                j += 1
                while j < k and nums[j-1] == nums[j]:
                    j += 1
                k -= 1
                while j < k and nums[k] == nums[k+1]:
                    k -= 1

            # skip the same values
            i += 1
            while i < len(nums)-2 and nums[i-1] == nums[i]:
                i += 1

        return triplets
