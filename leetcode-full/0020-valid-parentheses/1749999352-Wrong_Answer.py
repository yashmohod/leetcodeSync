class Solution:
    def isValid(self, s: str) -> bool:
        
        stk = []

        for i in s:
            if len(stk) == 0 :
                print(i)
                stk.append(i)
            else:
                last = stk.pop()
                stk.append(last)
                print(last,"L")
                if  ((last == "(" and i == ")") or 
                     (last == "{" and i == "}") or 
                     (last == "[" and i == "]")):
                    stk.pop()
                if i == "(" or i == "{" or i == "[":
                    stk.append(i)
                

        

        return len(stk) == 0 
