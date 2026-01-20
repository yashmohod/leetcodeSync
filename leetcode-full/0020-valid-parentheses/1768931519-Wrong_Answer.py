class Solution:
    def isValid(self, s: str) -> bool:
    
        q = deque([])
        m = {"}":"{","]":"[", ")":"("}
        for i in s :

            if i not in m.keys():
                q.append(i)
            else:
                if len(q) == 0:
                    return False
                else:
                    cur = q.pop()
                    if m[i] != cur:
                        return False
        return True
            
