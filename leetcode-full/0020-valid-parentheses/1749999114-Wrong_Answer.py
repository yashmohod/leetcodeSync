class Solution:
    def isValid(self, s: str) -> bool:
        
        stk = []

        for i in s:
            if len(stk) == 0 :
                stk.append(i)
            else:
                last = stk.pop()
                if  not ((last == "(" and i == ")") or 
                     (last == "{" and i == "}") or 
                     (last == "[" and i == "]")):
                     stk.append(last)

        

        return len(stk) == 0 
