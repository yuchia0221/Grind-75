# Middle of the Linked List

Problem can be found in [here](https://leetcode.com/problems/middle-of-the-linked-list/)!

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### [Solution](/Linked%20List/876-MiddleoftheLinkedList/solution.py): Fast and Slow Pointers

```python
def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    fast_pointer = slow_pointer = head

    while fast_pointer and fast_pointer.next:
        fast_pointer = fast_pointer.next.next
        slow_pointer = slow_pointer.next

    return slow_pointer
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)
