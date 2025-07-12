class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1 :
            return 1 
        count = 0 
        while n> count:
            
            count+=1
            n -= count 
        
        return count -1
