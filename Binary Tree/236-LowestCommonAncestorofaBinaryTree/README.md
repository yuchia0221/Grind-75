# Lowest Common Ancestor of a Binary Tree

Problem can be found in [here](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree)!

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### [Solution](/Binary%20Tree/236-LowestCommonAncestorofaBinaryTree/solution.py): Depth-First Search

```python
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Case 1: We have reached the children of leaf node
        if root is None:
            return root
        # Case 2: Found the targeted tree node
        if root == p or root == q:
            return root

        # Search for targeted tree nodes
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both targeted tree nodes are found, then return
        if left and right:
            return root
        # There are two scenarios: either one of the children found the targeted node and neither of them found.
        # For the first case: if we find p in left subtree and q is not found, this means that q is the child of p.
        # Therefore, we should return p as the lowest common ancestor.
        else:
            return left or right
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)
