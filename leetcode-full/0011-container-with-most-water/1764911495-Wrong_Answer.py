class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l,lmp =0,0
        r,rmp = len(height)-1,len(height)-1
        # lm,rm =height[lmp],height[rmp]
        maxA = 0

        while l<r:
            maxA = max(max(min(height[l],height[rmp])*(rmp-l),maxA),
                        max(min(height[r],height[lmp])*(r-lmp),maxA))
            if height[lmp] < height[l]:
                lmp =l
            if height[r] > height[rmp]:
                rmp =r
            
            l+=1
            r-=1
        
        return maxA




