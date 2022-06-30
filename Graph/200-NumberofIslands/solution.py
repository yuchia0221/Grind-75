from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row: int, column: int) -> None:
            exceed_boundaries = row < 0 or column < 0 or row >= number_of_row or column >= number_of_column
            if exceed_boundaries or grid[row][column] == "0":
                return

            grid[row][column] = "0"
            dfs(row-1, column)
            dfs(row+1, column)
            dfs(row, column-1)
            dfs(row, column+1)

        number_of_islands = 0
        number_of_row, number_of_column = len(grid), len(grid[0])
        for i in range(number_of_row):
            for j in range(number_of_column):
                if grid[i][j] == "1":
                    dfs(i, j)
                    number_of_islands += 1

        return number_of_islands
