class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        

        s = []
        res = -float('inf')
        for i in range(len(heights)):
            while s and heights[s[-1]] > heights[i]:
                c = s.pop()
                area = (i-c)* heights[c]
                res = max(area,res)
            s.append(i)

        if res == -float('inf'):
            for i in s:
                area = (len(heights)-i)* heights[i]
                res = max(area,res)
        
        return res
