# Lowest Common Ancestor of a Binary Search Tree

Problem can be found in [here](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree)!

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### [Solution](/Binary%20Search%20Tree/235-LowestCommonAncestorofaBinarySearchTree/solution.py): Depth-First Search

```python
def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    max_value, min_value = max(p.val, q.val), min(p.val, q.val)
    while root:
        if root.val > max_value:
            root = root.left
        elif root.val < min_value:
            root = root.right
        else:
            return root
```

Explanation: You can use the same [solution](/Binary%20Tree/236-LowestCommonAncestorofaBinaryTree/) to solve this problem. However, we can improve our time complexity by considering the properties of binary search tree, which is value on the left subtree's nodes < root's value < value on the right subtree's nodes.

Time Complexity: ![O(h)](<https://latex.codecogs.com/svg.image?\inline&space;O(h)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>), where h is the height of the binary search tree.
