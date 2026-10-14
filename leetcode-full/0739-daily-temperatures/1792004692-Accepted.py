class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0]*len(temperatures)

        s = deque([])

        for i in range(len(temperatures)):

            while s and s[-1][0]<temperatures[i] :
                temp,idx = s.pop()
                res[idx] = i-idx
            s.append([temperatures[i],i])
        return res



