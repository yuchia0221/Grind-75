# Linked List Cycle

Problem can be found in [here](https://leetcode.com/problems/linked-list-cycle/)!

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### [Solution](/Linked%20List/141-LinkedListCycle/solution.py): Fast Slow Pointers

```python
def hasCycle(head: Optional[ListNode]) -> bool:
    fast_pointer = slow_pointer = head

    while fast_pointer and fast_pointer.next:
        fast_pointer, slow_pointer = fast_pointer.next.next, slow_pointer.next
        if fast_pointer == slow_pointer:
            return True

    return False
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)
