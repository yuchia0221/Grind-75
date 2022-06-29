from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def search_and_fill(row: int, column: int) -> None:
            if image[row][column] == previos_color:
                image[row][column] = color
                if row + 1 < number_of_rows:
                    search_and_fill(row+1, column)
                if row >= 1:
                    search_and_fill(row-1, column)
                if column + 1 < number_of_columns:
                    search_and_fill(row, column+1)
                if column >= 1:
                    search_and_fill(row, column-1)

        number_of_columns, number_of_rows = len(image[0]), len(image)
        previos_color = image[sr][sc]
        if previos_color == color:
            return image

        search_and_fill(sr, sc)
        return image
