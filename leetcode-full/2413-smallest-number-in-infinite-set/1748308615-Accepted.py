class SmallestInfiniteSet:

    def __init__(self):
        
        self.removedSet = set()
        self.curSmol = 1

    def popSmallest(self) -> int:
        toRemove = self.curSmol

        self.removedSet.add(toRemove)
        while self.curSmol in self.removedSet:
            self.curSmol +=1

        return toRemove

    def addBack(self, num: int) -> None:
        if num in self.removedSet :
            self.removedSet.remove(num)

            if num < self.curSmol:
                self.curSmol = num
        



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
