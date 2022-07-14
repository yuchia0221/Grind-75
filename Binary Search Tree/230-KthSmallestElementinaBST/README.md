# Kth Smallest Element in a BST

Problem can be found in [here](https://leetcode.com/problems/kth-smallest-element-in-a-bst)!

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### [Solution](/Binary%20Search%20Tree/230-KthSmallestElementinaBST/solution.py): Depth-First Search

```python
def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    stack = []

    while True:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        k -= 1
        if not k:
            return root.val
        root = root.right
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), where n is the number of treenodes in the binary search tree.
