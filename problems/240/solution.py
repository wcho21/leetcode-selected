# Accepted: 152ms (7.84%), 22.94MB (17.36%)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        xlim = len(matrix[0])
        ylim = len(matrix)

        x = 0
        y = ylim-1

        while 0 <= x < xlim and 0 <= y < ylim:
            n = matrix[y][x]

            if n == target:
                return True

            if n < target:
                x += 1
            else:
                y -= 1

        return False
