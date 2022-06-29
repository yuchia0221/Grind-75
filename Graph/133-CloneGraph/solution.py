from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


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
