# Balanced Binary Tree

Problem can be found in [here](https://leetcode.com/problems/balanced-binary-tree)!

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### [Solution](/Binary%20Tree/110-BalancedBinaryTree/solution.py): Hash Table + Depth-First Search

```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        self.memo = {}
        subtrees_height_diff = abs(self.find_depth(root.left)-self.find_depth(root.right))
        is_tree_balanced = subtrees_height_diff < 2
        return is_tree_balanced and self.isBalanced(root.left) and self.isBalanced(root.right)

    def find_depth(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        if node not in self.memo:
            self.memo[node] = max(self.find_depth(node.left), self.find_depth(node.right)) + 1

        return self.memo[node]
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)
