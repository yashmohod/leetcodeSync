class SmallestInfiniteSet:

    def __init__(self):
        self.removed = set([])
        self.su = 1

    def popSmallest(self) -> int:
        
        if len(self.removed) == 0:
            res = self.su
            self.su +=1
            return res
        else:
            removedmin = min(self.removed)
            self.removed.remove(removedmin)
            return removedmin 

    def addBack(self, num: int) -> None:
        if num < self.su:
            self.removed.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
