# Accepted: 75ms (100.00%), 18.83MB (100.00MB)

class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        # BFS to find minimum distance
        visited: Set[int] = set() # visited x
        queue: Deque[Tuple[int, int]] = deque() # (x, distance)

        visited.add(x)
        queue.append((x, 0))

        while len(queue) > 0:
            x, n = queue.popleft()

            if x == y:
                return n

            if x+1 not in visited:
                visited.add(x+1)
                queue.append((x+1, n+1))
            if x > 1 and x-1 not in visited:
                visited.add(x-1)
                queue.append((x-1, n+1))
            if x % 5 == 0 and x // 5 not in visited:
                visited.add(x // 5)
                queue.append((x // 5, n+1))
            if x % 11 == 0 and x // 11 not in visited:
                visited.add(x // 11)
                queue.append((x // 11, n+1))

        return -1
