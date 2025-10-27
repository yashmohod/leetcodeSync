class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        

        b = 0
        l = 0
        for i in bank:
            c= i.count("1")
            if c > 0:
                b += c *l
                l=c
        
        return b

