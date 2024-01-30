# Accepted: 279ms (20.34%), 18.96MB (53.09%)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        WATER = "0"
        DY = [0, 0, -1, 1]
        DX = [-1, 1, 0, 0]

        def visitIsland(y: int, x: int) -> None:
            if not isInGrid(y, x) or grid[y][x] == WATER:
                return

            grid[y][x] = WATER

            for dy, dx in zip(DY, DX):
                visitIsland(y+dy, x+dx)

        def isInGrid(y, x) -> bool:
            return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

        # count islands

        count = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == WATER:
                    continue

                visitIsland(y, x)
                count += 1

        return count
