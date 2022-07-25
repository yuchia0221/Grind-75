from heapq import heappop, heappush
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
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
