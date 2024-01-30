// Accepted: 31ms (55.29%), 12.66MB (73.62%)

class Solution {
    char WATER = '0';

    void waterIsland(vector<vector<char>>& grid, const int x, const int y) {
        if (grid[y][x] == WATER) {
            return;
        }

        grid[y][x] = WATER;

        const int xLen = grid[0].size();
        const int yLen = grid.size();

        if (x > 0) {
            waterIsland(grid, x-1, y);
        }
        if (y > 0) {
            waterIsland(grid, x, y-1);
        }
        if (x < xLen-1) {
            waterIsland(grid, x+1, y);
        }
        if (y < yLen-1) {
            waterIsland(grid, x, y+1);
        }
    }
public:
    int numIslands(vector<vector<char>>& grid) {
        const int xLen = grid[0].size();
        const int yLen = grid.size();

        int numIslands = 0;
        for (int y = 0; y < yLen; ++y) {
            for (int x = 0; x < xLen; ++x) {
                if (grid[y][x] == WATER) {
                    continue;
                }

                waterIsland(grid, x, y);
                numIslands++;
            }
        }

        return numIslands;
    }
};
