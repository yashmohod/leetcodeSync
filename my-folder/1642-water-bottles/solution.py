class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        res = numBottles

        while numBottles>= numExchange:
            t = numBottles % numExchange
            c = numBottles // numExchange
            res +=numBottles // numExchange
            numBottles = t+c
            
        
        return res


