# 01 Matrix

Problem can be found in [here](https://leetcode.com/problems/01-matrix)!

### [Solution](/Graph/542-01Matrix/solution.py): Dynamic Programming

```python
def updateMatrix(matrix: List[List[int]]) -> List[List[int]]:
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
```

Explanation: Observe that for each 1-cell (the value of cell is one), its minimum distance to 0-cell (the value of cell is zero) must come from its four neighbors. We can perform a two-pass algorithm to solve this problem. In this problem, I decide to iterate the matrix from top->bottom & left->right and bottom->top & right->left. One may wonder whether the direction matters. The answer is "No" since if we iterate iterate the matrix from top->bottom & left->right, we are simply finding the shortest among all paths to the top/left/top-left of a given node.
As long as you search in all directions, your answer will be correct.

Time Complexity: ![O(m*n)](<https://latex.codecogs.com/svg.image?\inline&space;O(mn)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>), where m is the number of row and n is the number of column.
