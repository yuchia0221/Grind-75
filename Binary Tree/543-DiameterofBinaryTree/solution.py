from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
