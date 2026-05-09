class Node:
    def __init__(self,key,val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = {} 
        self.left = Node(None,None)
        self.right = Node(None,None)
        self.left.next = self.right
        self.right.prev = self.left


    def get(self, key: int) -> int:
        if key not in self.d :
            return -1

        self.d[key].prev.next = self.d[key].next
        self.d[key].next.prev = self.d[key].prev

        self.d[key].prev = self.right.prev
        self.right.prev.next = self.d[key]
        self.d[key].next = self.right
        self.right.prev = self.d[key]
        return self.d[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.get(key)
            self.d[key].val = value
        else:
            self.d[key] = Node(key,value)
     
            if len(self.d) > self.cap:
                cur = self.left.next
                self.left.next = cur.next
                cur.next.prev = self.left
                del self.d[cur.key]
            self.d[key].prev = self.right.prev
            self.d[key].prev.next = self.d[key]
            self.d[key].next = self.right
            self.right.prev = self.d[key]

           




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
