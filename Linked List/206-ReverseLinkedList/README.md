# Reverse Linked List

Problem can be found in [here](https://leetcode.com/problems/reverse-linked-list/)!

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### [Solution](/Linked%20List/206-Reverse-Linked-List/solution.py)

```python
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    previous_node = None
    while head:
        current_node = head
        head = head.next
        current_node.next = previous_node
        previous_node = current_node

    return previous_node
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)
