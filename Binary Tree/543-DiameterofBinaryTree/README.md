# Diameter of Binary Tree

Problem can be found in [here](https://leetcode.com/problems/diameter-of-binary-tree)!

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### [Solution](/Binary%20Tree/543-DiameterofBinaryTree/solution.py): Depth-First Search

```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.answer = 0
        self.find_diameter(root)
        return self.answer

    def find_diameter(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return -1

        left, right = self.find_diameter(node.left), self.find_diameter(node.right)
        self.answer = max(self.answer, 2+left+right)
        return 1 + max(left, right)
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)
