class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        l,s,ans = [],[],[]

        num1 = list(num1)
        num2 = list(num2)
        
        if len(num1)> len(num2):
            l,s = num1,num2
        else:
            l,s = num2,num1
        
        carry = 0 

        for i in range(1,len(s)+1):
            sum = int(s[-i]) + int(l[-i]) + carry 
            carry = sum // 10 
            ans.append(sum%10)

        for i in range(len(s)+1,len(l)+1):
            sum =int(l[-i]) + carry 
            carry = sum // 10 
            ans.append(sum%10)
        
        ans.reverse()
        res=""
        for i in range(len(ans)):
            res +=str(ans[i])
        return res

        

