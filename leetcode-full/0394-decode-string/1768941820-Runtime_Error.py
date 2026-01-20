class Solution:
    def decodeString(self, s: str) -> str:
        
        q = deque([])
        res = ""

        for i in s :
            if i == "]":
                r = ""
                while q[-1] != "[":
                    r = q.pop() +r
                n = ""
                while q and q[-1].isdigit():
                    n = q.pop()+n
                r = r * int(n)
                if q:
                    q.append(r)
                else:
                    res = res+r 
            else:
                q.append(i)
        
        for i in q:
            res += i
        return res
                

