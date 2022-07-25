# Merge k Sorted Lists

Problem can be found in [here](https://leetcode.com/problems/merge-k-sorted-lists)!

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### [Solution](/Heap/23-MergekSortedLists/solution.py): Heap

```python
def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if lists is None:
        return []

    heap = []
    for i in lists:
        if i is not None:
            heappush(heap, (i.val, id(i), i))

    dummy_head = current = ListNode()
    while heap:
        node = heappop(heap)[2]
        current.next = current = node
        if node.next:
            next_node = node.next
            heappush(heap, (current.val, id(next_node), next_node))

    return dummy_head.next
```

Time Complexity: ![O(nlogk)](<https://latex.codecogs.com/svg.image?\inline&space;O(nlogk)>), Space Complexity: ![O(k)](<https://latex.codecogs.com/svg.image?\inline&space;O(k)>), where n is the number of nodes in all linked lists and k is the number of linked lists.
