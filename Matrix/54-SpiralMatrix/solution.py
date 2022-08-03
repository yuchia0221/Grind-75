from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output_list = []
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1

        while top < bottom and left < right:
            for column in range(left, right):
                output_list.append(matrix[top][column])

            for row in range(top, bottom):
                output_list.append(matrix[row][right])

            for column in range(right, left, -1):
                output_list.append(matrix[bottom][column])

            for row in range(bottom, top, -1):
                output_list.append(matrix[row][left])

            top, bottom, left, right = top+1, bottom-1, left+1, right-1

        for row in range(top, bottom+1):
            for column in range(left, right+1):
                output_list.append(matrix[row][column])

        return output_list
