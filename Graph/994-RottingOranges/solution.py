from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def BFS(row, column):
            if row > 0 and grid[row-1][column] == 1:
                grid[row-1][column] = 2
                fresh_oranges -= 1
                rotten_oranges.append([row-1, column])
            if row < number_of_row-1 and grid[row+1][column] == 1:
                grid[row+1][column] = 2
                fresh_oranges -= 1
                rotten_oranges.append([row+1, column])
            if column > 0 and grid[row][column-1] == 1:
                grid[row][column-1] = 2
                fresh_oranges -= 1
                rotten_oranges.append([row, column-1])
            if column < number_of_column-1 and grid[row][column+1] == 1:
                grid[row][column+1] = 2
                fresh_oranges -= 1
                rotten_oranges.append([row, column+1])

        rotten_oranges = deque()
        counter = fresh_oranges = 0
        number_of_row, number_of_column = len(grid), len(grid[0])
        for i in range(number_of_row):
            for j in range(number_of_column):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    rotten_oranges.append([i, j])

        while rotten_oranges and fresh_oranges:
            for _ in range(len(rotten_oranges)):
                row, column = rotten_oranges.popleft()
                BFS(row, column)
            counter += 1

        return counter if fresh_oranges == 0 else -1
