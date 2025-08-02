class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        s = []
        ans =  [0]*len(temperatures)
        for i in range(len(temperatures)):
            cur = 1
            t = i-1
            while s and s[-1] < temperatures[i]:
                s.pop()
                ans[t] = cur 
                t -=1 
                cur +=1

            s.append(i)
        
        return ans 
