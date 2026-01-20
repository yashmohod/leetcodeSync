class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.res = []
        for i in range(min(len(v1),len(v2))) :
            self.res.append(v1[i])
            self.res.append(v2[i])
        if len(v1)>len(v2):
            for i in range(len(v2),len(v1)):
                self.res.append(v1[i])
        elif len(v1)<len(v2) :
            for i in range(len(v1),len(v2)):
                self.res.append(v2[i]) 
        self.res = deque(self.res)       
    def next(self) -> int:
        return self.res.popleft()

    def hasNext(self) -> bool:
        return len(self.res)>0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
