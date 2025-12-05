class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if len(s)< numRows:
            return s

        res = [[] for _ in range(numRows)]
        t = True
        c = 1
        for i in s :
            res[c-1].append(i)
            if t :
                c+=1
            else:
                c-=1
            if c == numRows:
                t=False
            if c == 1:
                t =True
        
        res = ["".join(i) for i in res]
        return "".join(res)

