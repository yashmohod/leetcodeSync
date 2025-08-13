class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        c = 0 

        while 3**c <= n :

            if 3**c == n:
                return True
            else:
                c+=1


        return False
