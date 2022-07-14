# Validate Binary Search Tree

Problem can be found in [here](https://leetcode.com/problems/validate-binary-search-tree)!

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### [Solution](/Binary%20Search%20Tree/98-ValidateBinarySearchTree/solution.py): Depth-First Search

```python
def isValidBST(root: Optional[TreeNode], ceil: int = float("inf"), floor: int = float("-inf")) -> bool:
    if not root:
        return True

    if floor < root.val < ceil:
        # Check if the left subtree and the right subtree meets the requirements of the BST
        return self.isValidBST(root.left, root.val, floor) and self.isValidBST(root.right, ceil, root.val)
    else:
        return False
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), where n is the number of treenodes in the binary search tree.
