class ListNode:
    def __init__(self, key: int = None, value: int = None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_table = dict()
        self.dummy_head = ListNode()
        self.dummy_tail = ListNode()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def get(self, key: int) -> int:
        try:
            value = self.hash_table[key].value
            self.remove(self.hash_table[key])
            self.insert(self.hash_table[key])
            return value
        except KeyError:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_table:
            self.remove(self.hash_table[key])
        if self.capacity == 0:
            delete_node = self.dummy_head.next
            del self.hash_table[delete_node.key]
            self.remove(delete_node)

        new_node = ListNode(key, value)
        self.insert(new_node)
        self.hash_table[key] = new_node

    def remove(self, node: ListNode) -> None:
        self.capacity += 1
        previous_node, next_node = node.prev, node.next
        next_node.prev = previous_node
        previous_node.next = next_node

    def insert(self, node: ListNode) -> None:
        self.capacity -= 1
        previous_node = self.dummy_tail.prev
        self.dummy_tail.prev = previous_node.next = node
        node.prev, node.next = previous_node, self.dummy_tail
