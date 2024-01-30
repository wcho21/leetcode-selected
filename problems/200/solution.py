# Accepted: 214ms (99.43%), 19.48MB (64.49%)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        WATER = "0"

        xLen = len(grid[0])
        yLen = len(grid)

        def waterIsland(x: int, y: int) -> None:
            if grid[y][x] == WATER:
                return

            grid[y][x] = WATER

            if x > 0:
                waterIsland(x-1, y)
            if y > 0:
                waterIsland(x, y-1)
            if x < xLen-1:
                waterIsland(x+1, y)
            if y < yLen-1:
                waterIsland(x, y+1)

        numIslands = 0
        for y in range(yLen):
            for x in range(xLen):
                if grid[y][x] == WATER:
                    continue

                waterIsland(x, y)
                numIslands += 1

        return numIslands
