class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        top = -1

        l,r = 0,len(height)-1

        while l<r:
            wat = abs(r-l) * min(height[l],height[r]) 
            print(wat,l,r)
            if wat > top :
                top = wat
            else:
                if r > l:
                    l+=1
                else:
                    r-=1
        
        return top 

        
