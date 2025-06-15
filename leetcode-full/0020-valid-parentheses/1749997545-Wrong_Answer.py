class Solution:
    def isValid(self, s: str) -> bool:
        
        a,b,c=0,0,0

        for i in s:
            if i == "(":
                a+=1
            if i == "{":
                b+=1
            if i == "[":
                c+=1

            if i == ")":
                a-=1
            if i == "}":
                b-=1
            if i == "]":
                c-=1
        
        print(a,b,c)
        print(a == 0 , b == 0 , c == 0 )
        return a == 0 and b == 0 and c == 0 
