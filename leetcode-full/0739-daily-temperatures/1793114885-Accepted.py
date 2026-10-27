class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        N = len(temperatures)

        for i in range(N):
            while s and temperatures[s[-1]] <temperatures[i]:
                x=s.pop()
                temperatures[x] = i-x            
            s.append(i)
        while s :
            i = s.pop()
            temperatures[i] = 0
        return temperatures



