class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects

    def pick(self) -> List[int]:
        
        region = random.randint(0,len(self.rects)-1)

        x = random.randint(self.rects[region][0],self.rects[region][2]-1)
        y = random.randint(self.rects[region][1],self.rects[region][3]-1)

        return [x,y]



# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
