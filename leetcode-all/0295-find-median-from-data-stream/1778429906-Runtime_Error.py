class MedianFinder:

    def __init__(self):
        self.d = {}
        self.size = 0

    def addNum(self, num: int) -> None:
        self.d[num] = self.d.get(num,0)+1
        self.size +=1

    def findMedian(self) -> float:
        half = int(self.size//2) if self.size %2 ==0 else int(self.size//2) +1
        print(self.d,half)
        som = 0
        prev = -1
        for key in self.d.keys():
            if som > half:
                return prev
            elif som == half:
                return (prev+key)/2 if self.size %2 ==0 else prev
            som += self.d[key]
            prev = key



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
