from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode], ceil: int = float("inf"), floor: int = float("-inf")) -> bool:
        if not root:
            return True

        if floor < root.val < ceil:
            return self.isValidBST(root.left, root.val, floor) and self.isValidBST(root.right, ceil, root.val)
        else:
            return False
