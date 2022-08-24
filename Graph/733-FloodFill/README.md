# Flood Fill

Problem can be found in [here](https://leetcode.com/problems/flood-fill)!

### [Solution](/Graph/733-FloodFill/solution.py): Depth-First Search

```python
def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
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
```

Explanation: To solve this problem, we need to perform depth-first search (DFS). Notice that when we need to search in 4 directions, we need to check whether exceeeds the boundaries.

Time Complexity: ![O(m * n)](<https://latex.codecogs.com/svg.image?\inline&space;O(m\cdot&space;n)>), Space Complexity: ![O(m * n)](<https://latex.codecogs.com/svg.image?\inline&space;O(m\cdot&space;n)>) for recursion stack, where m is the number of row and n is the number of column.
