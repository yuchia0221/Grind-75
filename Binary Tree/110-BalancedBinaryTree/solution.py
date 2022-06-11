from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        self.memo = {}
        is_root_balanced = abs(self.find_depth(root.left), self.find_depth(root.right)) < 2
        return is_root_balanced and self.isBalanced(root.left) and self.isBalanced(root.right)

    def find_depth(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        if node not in self.memo:
            self.memo[node] = max(self.find_depth(node.left), self.find_depth(node.right)) + 1

        return self.memo[node]
