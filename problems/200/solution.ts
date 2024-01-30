// Accepted: 68ms (89.09%), 45.61MB (76.38%)

function numIslands(grid: string[][]): number {
    const WATER = "0";

    const xLen = grid[0].length;
    const yLen = grid.length;

    const waterIsland = (x: number, y: number): void => {
        if (grid[y][x] === WATER) {
            return;
        }

        grid[y][x] = WATER;

        if (x > 0) {
            waterIsland(x-1, y);
        }
        if (y > 0) {
            waterIsland(x, y-1);
        }
        if (x < xLen-1) {
            waterIsland(x+1, y);
        }
        if (y < yLen-1) {
            waterIsland(x, y+1);
        }
    };

    let numIslands = 0;
    for (let y = 0; y < yLen; ++y) {
        for (let x = 0; x < xLen; ++x) {
            if (grid[y][x] === WATER) {
                continue;
            }

            waterIsland(x, y);
            numIslands++;
        }
    }

    return numIslands;
};
