# Accepted: 50ms (28.12%), 17.31MB (21.57%)

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def logKey(log: str) -> Tuple[int, str, str]:
            identifier, content = log.split(" ", 1)
            if content[0].isdigit():
                return (1, "", "")
            return (0, content, identifier)

        reorderedLogs = list(sorted(logs, key=logKey))
        return reorderedLogs
