# Accepted: 91ms (83.38%), 20.78MB (42.76%)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStrs = list(map(lambda s: "".join(sorted(s)), strs))

        anagramMap: Dict[str, List[str]] = defaultdict(list)
        for sortedString, string in zip(sortedStrs, strs):
            anagramMap[sortedString].append(string)

        anagramGroups = list(anagramMap.values())
        return anagramGroups
