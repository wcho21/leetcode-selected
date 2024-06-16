// Accepted: 73ms (73.70%), 52.92MB (78.15%)

function numIslands(grid: string[][]): number {
    const WATER = "0";
    const DY = [0, 0, -1, 1];
    const DX = [-1, 1, 0, 0];

    function visitIsland(y: number, x: number): void {
        if (!isInGrid(y, x) || grid[y][x] == WATER) {
            return;
        }

        grid[y][x] = WATER;

        for (let i = 0; i < 4; ++i) {
            visitIsland(y+DY[i], x+DX[i]);
        }
    }

    function isInGrid(y: number, x: number): boolean {
        return 0 <= y && y < grid.length && 0 <= x && x < grid[0].length;
    }

    let count = 0;
    for (let y = 0; y < grid.length; ++y) {
        for (let x = 0; x < grid[0].length; ++x) {
            if (grid[y][x] == WATER) {
                continue;
            }

            ++count;
            visitIsland(y, x);
        }
    }

    return count;
};
