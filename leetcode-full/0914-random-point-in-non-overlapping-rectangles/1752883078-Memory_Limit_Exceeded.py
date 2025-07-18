import random
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.opts = []

        for rect in rects:
            for x in range(rect[0],rect[2]):
                for y in range(rect[1],rect[3]):
                    self.opts.append([x,y])
        

    def pick(self) -> List[int]:

        idx = random.randint(0,len(self.opts)-1)
        return self.opts[idx]

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
