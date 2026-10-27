class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
       

        s = []
        N = len(temperatures)
        res = [0]*N

        for i in range(N):

            while s and s[-1][1] <temperatures[i]:
                x,t=s.pop()
                res[x] = i-x
            
            s.append([i,temperatures[i]])

        return res



