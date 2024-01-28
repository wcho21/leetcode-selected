# Accepted: 99ms (38.98%), 27.16MB (5.22%)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        countToNums = defaultdict(list)
        for num, count in counts.items():
            countToNums[count].append(num)

        tops = []
        for count in reversed(range(1, len(nums)+1)):
            if countToNums[count] == 0:
                continue

            for num in countToNums[count]:
                tops.append(num)
                k -= 1

            if k <= 0:
                break

        return tops
