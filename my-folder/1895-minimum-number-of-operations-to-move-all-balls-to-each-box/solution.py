class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        b = list(boxes)
        n = len(boxes)
        res =[0]*n
        
        prf,ball = 0,0
        for i in range(n):
            res[i] = prf + ball
            prf +=ball
            ball += int(b[i])
            
        
        prf,ball = 0,0
        for i in range(n-1,-1,-1):
            res[i] += prf + ball
            prf +=ball
            ball += int(b[i])
            
        
        return res
            
