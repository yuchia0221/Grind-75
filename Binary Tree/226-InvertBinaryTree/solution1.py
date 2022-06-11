from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

