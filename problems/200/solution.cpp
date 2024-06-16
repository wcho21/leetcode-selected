// Accepted: 23ms (88.33%), 15.73MB (74.83%)

class Solution {
private:
    char WATER = '0';
    int DY[4] = { 0, 0, -1, 1 };
    int DX[4] = { -1, 1, 0, 0 };

    void visitIsland(vector<vector<char>>& grid, int y, int x) {
        if (!isInGrid(grid, y, x) || grid[y][x] == WATER) {
            return;
        }

        grid[y][x] = WATER;

        for (int i = 0; i < 4; ++i) {
            visitIsland(grid, y+DY[i], x+DX[i]);
        }
    }

    bool isInGrid(vector<vector<char>>& grid, int y, int x) {
        return 0 <= x && x < grid[0].size() && 0 <= y && y < grid.size();
    }

public:
    int numIslands(vector<vector<char>>& grid) {
        int count = 0;

        for (int y = 0; y < grid.size(); ++y) {
            for (int x = 0; x < grid[0].size(); ++x) {
                if (grid[y][x] == WATER) {
                    continue;
                }

                ++count;
                visitIsland(grid, y, x);
            }
        }

        return count;
    }
};
