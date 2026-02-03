class Solution:
    def isValid(self, s: str) -> bool:
    
        r = {"}":"{","]":"[",")":"("}
        t = deque([])

        for i in s:
            if i in r:
                if t and t[-1] == r[i]:
                    t.pop()
                else:
                    t.append(i)
            else:
                t.append(i)

        return len(t) == 0 
            
