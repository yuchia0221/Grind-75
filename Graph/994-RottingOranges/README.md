# Rotting Oranges

Problem can be found in [here](https://leetcode.com/problems/rotting-oranges)!

### [Solution](/Graph/994-RottingOranges/solution.py): Breadth-First Search

```python
def orangesRotting(grid: List[List[int]]) -> int:
    def BFS(row, column):
        """ Check whether its neighbors are fresh. If so, update and push into queue. """
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

    # Initialization
    rotten_oranges = deque()
    counter = fresh_oranges = 0
    number_of_row, number_of_column = len(grid), len(grid[0])
    for i in range(number_of_row):
        for j in range(number_of_column):
            if grid[i][j] == 1:
                fresh_oranges += 1
            elif grid[i][j] == 2:
                rotten_oranges.append([i, j])

    # Simulate the rotten process
    while rotten_oranges and fresh_oranges:
        for _ in range(len(rotten_oranges)):
            row, column = rotten_oranges.popleft()
            BFS(row, column)
        counter += 1

    return counter if fresh_oranges == 0 else -1
```

Explanation: In the initial stage, we need to iterate the whole grid once to compute the number of fresh oranges and the location of rotten oranges. In each iteration (minute), we perform a one-level BFS (breadth-first search) for all rotten oranges. If we find a fresh orange next to a rotten orange, we update a fresh orange to rotten one and the number of remaining fresh oranges. Once the number of fresh oranges is 0 or there are no rotten oranges in the queue, we know the algorithm is finished.

Time Complexity: ![O(m * n)](<https://latex.codecogs.com/svg.image?\inline&space;O(m\cdot&space;n)>), Space Complexity: ![O(m * n)](<https://latex.codecogs.com/svg.image?\inline&space;O(m\cdot&space;n)>), where m is the number of rows and n is the number of columns since there may be m*n rotten oranges in the worst case initially.
