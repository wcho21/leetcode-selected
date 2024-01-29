# Accepted: 45ms (42.62%), 16.56MB (59.98%)

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastOccurIndex: Dict[str, int] = {ch: i for i, ch in enumerate(s)}

        visited: Set[int] = set()
        ordered: List[str] = []

        for i in range(len(s)):
            ch = s[i]

            if ch in visited:
                continue

            # pop characters
            while len(ordered) > 0:
                top = ordered[-1]
                if i >= lastOccurIndex[top]: # last occurrence
                    break
                if ch > top: # in lexicographical order
                    break

                visited.remove(top)
                ordered.pop()

            # insert current character
            visited.add(ch)
            ordered.append(ch)

        return "".join(ordered)
