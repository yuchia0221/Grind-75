# Clone Graph

Problem can be found in [here](https://leetcode.com/problems/clone-graph)!

```python
# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
```

### [Solution](/Graph/133-CloneGraph/solution.py): Breadth-First Search + Hash Table

```python
class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if node is None:
            return node

        queue = deque([node])
        clones = {node.val: Node(node.val)}
        while queue:
            current = queue.popleft()
            current_clone = clones[current.val]
            for neighbor in current.neighbors:
                if neighbor.val not in clones:
                    clones[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)

                current_clone.neighbors.append(clones[neighbor.val])

        return clones[node.val]
```

Explanation: Simply perform breadth-first search (BFS) to solve this problem and use a hash table to track vistied and cloned nodes.

Time Complexity: ![O(V + E)](<https://latex.codecogs.com/svg.image?\inline&space;O(V + E)>), Space Complexity: ![O(V)](<https://latex.codecogs.com/svg.image?\inline&space;O(V)>), where V is the total number of nodes and E is the total number of edges.
