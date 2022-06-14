# Maximum Depth of Binary Tree

Problem can be found in [here](https://leetcode.com/problems/maximum-depth-of-binary-tree)!

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### [Solution](/Binary%20Tree/104-MaximumDepthofBinaryTree/solution.py): Depth-First Search

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
```

Explanation: If we want to find out the maximum depth of an arbitrary binary tree node, we need to calculate the depth of its left child and right child. Therefore, to return the depth of a binary tree, we just need to iterate from the top of root to the leaf.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(h)](<https://latex.codecogs.com/svg.image?\inline&space;O(h)>) for the recursive stack, where h is the height of the binary tree. In worst case, h will be n for an unbalanced binary tree.
