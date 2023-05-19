from typing import List
from future import __annotations__
from collections import deque


class Node:
    __slots__ = ["nodes", "marked", "value"]

    def __init__(self):
        self.nodes: List[Node | None] = [None] * 26
        self.marked = False
        self.value = 0


class MapSum:
    def __init__(self):
        self.head = Node()

    def insert(self, key: str, val: int) -> None:
        cur: Node = self.head
        for char in key[:-1]:
            if cur.nodes[ord(char) - ord("a")] is None:
                new_node = Node()
                cur.nodes[ord(char) - ord("a")] = new_node
            cur = cur.nodes[ord(char) - ord("a")]

        last = key[-1]
        if cur.nodes[ord(last) - ord("a")] is None:
            new_node = Node()
            cur.nodes[ord(last) - ord("a")] = new_node
        cur = cur.nodes[ord(last) - ord("a")]
        cur.marked = True
        cur.value = val

    def sum(self, prefix: str) -> int:
        cur: Node = self.head
        sum = 0
        for char in prefix:
            if cur.nodes[ord(char) - ord("a")] is None:
                return sum
            cur = cur.nodes[ord(char) - ord("a")]

        queue = list()
        queue.append(cur)
        while len(queue) > 0:
            node = queue.pop()
            if node.marked:
                sum += node.value

            for el in node.nodes:
                if el is not None:
                    queue.append(el)
        return sum
