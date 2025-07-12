class Solution:
    def toHex(self, num: int) -> str:
        
        if num >-1:
            return hex(num)[2:]
        else:
            return hex(2**32 + num)[2:]
        

