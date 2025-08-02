class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        

        s = []
        res = 0 

        for i,h in enumerate(heights):
            start = 1 
            while s and s[-1][1] > h:
                idx,ch = stack.pop()
                res = max(res,ch *(i-idx))
                start = idx
            s.append(start)
        
        for i,h in s:
            res = max(res,h*(len(heights)-i))

        return res
