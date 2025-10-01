import numpy as np
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.outcomes = [i for i in range(len(rects))]
        self.probabilities = []
        self.totprob = 0
        for i in self.outcomes:
            h = rects[i][3]-rects[i][1]
            w = rects[i][2]-rects[i][0]
            self.totprob +=h*w
            self.probabilities.append(h*w)
        for i in range(len(self.probabilities)):
            self.probabilities[i] /=self.totprob

    def pick(self) -> List[int]:
        
        region = np.random.choice(self.outcomes, p=self.probabilities) -1

        x = random.randint(self.rects[region][0],self.rects[region][2])
        y = random.randint(self.rects[region][1],self.rects[region][3])

        return [x,y]



# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
