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
        # The reason to return -1 is to compensate for the addition of 2 in the following lines
        if node is None:
            return -1

        left, right = self.find_diameter(node.left), self.find_diameter(node.right)
        # We need to add 2 for calculating the diameter is because
        # we need to count the path from left and right subtrees to root, respectively.
        self.answer = max(self.answer, 2+left+right)
        return 1 + max(left, right)
```

Explanation: The intuitive solution is to check "every" tree node to calculate the diameter of a binary tree. However, the algorithm will run in ![O(n^2)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^2)>) time, which sucks. To improve the algorithm's time complexity, we can perform a depth-first search (DFS) to store the previous result through recursion.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(h)](<https://latex.codecogs.com/svg.image?\inline&space;O(h)>) for the recursive stack, where h is the height of the binary tree. In worst case, h will be n for an unbalanced binary tree. Therefore, the space complexity will be ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>).
