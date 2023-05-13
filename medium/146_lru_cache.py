class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity
        self.head = Node((0, 0))
        self.tail = Node((0, 0))
        self.head.prev = self.tail
        self.tail.next = self.head

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self.remove(node)
            self.add(node)
            return node.val[1]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.remove(self.dict[key])
        n = Node((key, value))
        self.dict[key] = n
        self.add(n)
        if len(self.dict) > self.capacity:
            n = self.tail.next
            self.remove(n)
            del self.dict[n.val[0]]

    def remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def add(self, node):
        p = self.head.prev
        p.next = node
        self.head.prev = node
        node.prev = p
        node.next = self.head


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
