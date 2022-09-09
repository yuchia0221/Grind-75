# Binary Tree Level Order Traversal

Problem can be found in [here](https://leetcode.com/problems/binary-tree-level-order-traversal)!

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### [Solution](/Binary%20Tree/102-BinaryTreeLevelOrderTraversal/solution.py): Breadth-First Search

```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue, output_list = collections.deque([root]), []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            output_list.append(level)

        return output_list
```

Explanation: We can solve this problem by using breadth-first search (BFS). To support performing BFS on the binary tree, we need to use a queue. As we iterate the whole binary tree, we will get the level-order traversal of given binary tree.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)
