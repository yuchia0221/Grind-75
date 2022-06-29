from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        distance = [[float("inf") for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if matrix[row][column] == 0:
                    distance[row][column] = 0
                else:
                    if row > 0:
                        distance[row][column] = min(distance[row][column], distance[row-1][column] + 1)
                    if column > 0:
                        distance[row][column] = min(distance[row][column], distance[row][column-1] + 1)

        for row in range(len(matrix)-1, -1, -1):
            for column in range(len(matrix[0])-1, -1, -1):
                if row < len(matrix)-1:
                    distance[row][column] = min(distance[row][column], distance[row+1][column] + 1)
                if column < len(matrix[0])-1:
                    distance[row][column] = min(distance[row][column], distance[row][column+1] + 1)

        return distance
