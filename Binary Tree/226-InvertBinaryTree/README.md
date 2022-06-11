# Inveret Binary Tree

Problem can be found in [here](https://leetcode.com/problems/invert-binary-tree)!

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### [Solution1](/Binary%20Tree/226-InvertBinaryTree/solution1.py): DFS(Recursion)

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.inverter(root.left, root.right)
        return root

    def inverter(self, left_child: Optional[TreeNode], right_child: Optional[TreeNode]) -> List[TreeNode]:
        if left_child is not None:
            left_child.left, left_child.right = self.inverter(left_child.left, left_child.right)
        if right_child is not None:
            right_child.left, right_child.right = self.inverter(right_child.left, right_child.right)

        return right_child, left_child
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

### [Solution2](/Binary%20Tree/226-InvertBinaryTree/solution2.py): Improved Solution 1

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)
