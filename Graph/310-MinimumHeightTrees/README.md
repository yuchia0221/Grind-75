# Minimum Height Trees

Problem can be found in [here](https://leetcode.com/problems/minimum-height-trees)!

### [Solution](/Graph/310-MinimumHeightTrees/solution.py): Topological Sort

```python
def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]:
    # Edge Cases: only one node in the graph
    if not edges:
        return [0]

    # Build up adjacency list
    adjacency_list = [set() for _ in range(n)]
    for start, end in edges:
        adjacency_list[start].add(end)
        adjacency_list[end].add(start)

    # Find the leaf nodes of the tree
    leaves = []
    for index, neighbors in enumerate(adjacency_list):
        if len(neighbors) == 1:
            leaves.append(index)

    # Remove leaf nodes until there is less than or equal to 2 nodes
    leaf_reamining = n
    while leaf_reamining > 2:
        new_leaves = []
        leaf_reamining -= len(leaves)
        for _ in range(len(leaves)):
            leaf_node = leaves.pop()
            neighbor = adjacency_list[leaf_node].pop()
            adjacency_list[neighbor].remove(leaf_node)
            if len(adjacency_list[neighbor]) == 1:
                new_leaves.append(neighbor)
        leaves = new_leaves

    return leaves
```

Time Complexity: ![O(N)](<https://latex.codecogs.com/svg.image?\inline&space;O(N)>), Space Complexity: ![O(N)](<https://latex.codecogs.com/svg.image?\inline&space;O(N)>), where N is the number of nodes.
