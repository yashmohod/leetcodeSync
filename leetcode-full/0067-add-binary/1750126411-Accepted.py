class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        a = list(a)
        b = list(b)
        carry = 0
        if len(b) > len(a): 
            a,b = b,a

        for i in range(1,len(a)+1):  
            cur = 0
            if len(b) >= i:
                cur = carry + int(a[-i]) + int(b[-i])
            else:   
                cur = carry + int(a[-i]) 

            carry = cur // 2  
            a[-i] = cur % 2 
            print(a[-i],carry)
            

        if carry > 0: 
            a = [carry] + a  
        ans=""
        for i in a:
            ans+= str(i)

        return ans
