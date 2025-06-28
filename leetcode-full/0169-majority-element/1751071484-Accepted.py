class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        tb = {}

        for i in nums:
            if i in tb:
                tb[i] +=1
            else:
                tb[i] = 1
            
        gx,gy = 0,0
        for x,y in tb.items():
            print(x,y)
            if gy < y :
                gx = x
                gy = y 
        
        return gx 
