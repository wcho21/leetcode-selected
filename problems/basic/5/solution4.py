# Accepted: 90ms (97.91%), 17.52MB (21.09%)

# Manacher's algorithm

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # to check even-number size palindromes, insert dummay characters
        string = "#" + "#".join(s) + "#"

        n = len(string)
        radii = [0] * n
        center = 0 # center of recent large palindrome
        rbound = 0 # the greatest index that recent large palindrome have accessed

        for i in range(n):
            # use the precalculated radius at index mirrored with respect to center
            if 0 < i < rbound:
                # get index mirrored with respect to center
                mirrored = 2 * center - i
                # we haven't checked characters beyond rbound
                # so ensure that the radius does not take the index i beyond rbound
                radii[i] = min(radii[mirrored], rbound - i)

            # get the longest palindrome, centered at i
            left = i - radii[i]
            right = i + radii[i]
            while left > 0 and right < n-1 and string[left-1] == string[right+1]:
                left -= 1
                right += 1
                radii[i] += 1

            # update to make next indices use the previous calculation
            if right > rbound:
                rbound = right
                center = i

        radius, i = max((radius, i) for i, radius in enumerate(radii))
        beg = (i - radius) // 2
        end = (i + radius) // 2
        return s[beg:end]
