# Serialize and Deserialize Binary Tree

Problem can be found in [here](https://leetcode.com/problems/serialize-and-deserialize-binary-tree)!

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### [Solution](/Binary%20Tree/297-SerializeandDeserializeBinaryTree/solution.py): Breadth-First Search

```python
class Codec:
    def serialize(self, root: Optional[TreeNode]) -> Optional[str]:
        if root is None:
            return ""

        # Perfrom BFS with queue. If a node's child is None, represent it as #.
        output_list = []
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    output_list.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    output_list.append("#")

        return " ".join(output_list)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 0:
            return None

        i = 0
        binary_tree = data.split()
        root = TreeNode(binary_tree[0])
        queue = deque([root])
        while queue:
            # If you pop a node, its child will be at i+1 and i+2 if there is one.
            node = queue.popleft()
            i += 1
            if i < len(binary_tree) and binary_tree[i] != "#":
                node.left = TreeNode(int(binary_tree[i]))
                queue.append(node.left)

            i += 1
            if i < len(binary_tree) and binary_tree[i] != "#":
                node.right = TreeNode(int(binary_tree[i]))
                queue.append(node.right)

        return root
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>).
