class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        count = 0 
        while n> count:
            n -= count 
            count+=1
        
        return count -1
