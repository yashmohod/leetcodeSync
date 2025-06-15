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

            if i == "}":
                a-=1
            if i == ")":
                b-=1
            if i == "]":
                c-=1
        
        return a+b+c == 0
