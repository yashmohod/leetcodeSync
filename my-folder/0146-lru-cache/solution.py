class Node:
    def __init__(self,key, value):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.size = abs(capacity)
        self.dict = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, newNode: Node):
        prev, next = self.tail.prev, self.tail
        prev.next = next.prev = newNode
        newNode.next = next
        newNode.prev = prev

    def remove(self,curNode):
        prev, next = curNode.prev, curNode.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key in self.dict:
            self.remove(self.dict[key])
            self.insert(self.dict[key])
            return self.dict[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.remove(self.dict[key])
        self.dict[key] = Node(key,value)
        self.insert(self.dict[key])

        if len(self.dict)> self.size:
            lru = self.head.next
            self.remove(lru)
            del self.dict[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

