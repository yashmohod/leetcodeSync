class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        c = 1 

        while c <= num/2:
            if c**2 == num:
                return True
            c+=1
        return False
