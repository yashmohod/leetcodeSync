import random
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects

    def pick(self) -> List[int]:

        idx = random.randint(0,len(self.rects)-1)
        x = random.uniform(self.rects[idx][0],self.rects[idx][2])
        y = random.uniform(self.rects[idx][1],self.rects[idx][3])

        return [x,y]

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
