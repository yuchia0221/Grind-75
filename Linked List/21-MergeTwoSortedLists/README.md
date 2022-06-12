# Merge Two Sorted Lists

Problem can be found in [here](https://leetcode.com/problems/merge-two-sorted-lists)!

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### [Solution](/Linked%20List/21-Merge-Two-Sorted-Lists/solution.py): Dummy Head

```python
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy_head = current_node = ListNode()

    while list1 and list2:
        if list1.val < list2.val:
            current_node.next = list1
            list1 = list1.next
        else:
            current_node.next = list2
            list2 = list2.next
        current_node = current_node.next

    current_node.next = list1 if list1 else list2
    return dummy_head.next
```

Time Complexity: ![O(n+m)](<https://latex.codecogs.com/svg.image?\inline&space;O(n+m)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>), where n and m are the length of list1 and list2, respectively.
