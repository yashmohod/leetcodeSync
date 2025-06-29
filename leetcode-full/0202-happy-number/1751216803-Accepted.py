class Solution:
    def isHappy(self, n: int) -> bool:
        
        n = str(n)

        # if len(n) ==1:
        #     if int(n)**2 == 1:
        #         return True
        #     else:
        #         return False
        check =[int(n)]
        while n != "1" :

            res = 0 

            for i in n:
                res += int(i) **2
            
            if res in check:
                return False
            else:
                check.append(res)
            n = str(res)
        
        return True
