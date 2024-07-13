# Accepted: 43ms (82.47%), 16.78MB (21.83%)

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        commons = []

        set1 = set(nums1)
        set2 = set(nums2)
        for n in set2:
            if n in set1:
                commons.append(n)

        return commons
