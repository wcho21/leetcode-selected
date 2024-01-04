# Accepted: 42ms (66.89%), 17.42MB (12.65%)

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        bannedSet = set(banned)

        searched = findall(r"[a-z]+", paragraph.lower())
        counts = Counter(searched)

        for word, _ in counts.most_common():
            if word not in bannedSet:
                return word

        raise Exception("no word found")
