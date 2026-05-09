class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = {} 
        self.used = deque([])

    def get(self, key: int) -> int:
        res = self.d.get(key,-1)
        if res != -1:
            if key in self.used:
                self.used.remove(key)
            self.used.append(key)
        return res

    def put(self, key: int, value: int) -> None:
        self.d[key] = value
        if key in self.used:
            self.used.remove(key)
        self.used.append(key)
        if len(self.d)>self.cap:
            lru = self.used.popleft() if self.used else None
            if lru: 
                del self.d[lru]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
