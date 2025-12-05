class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or len(s)<= numRows:
            return s

        res = [[] for _ in range(numRows)]
        t = True
        c = 0
        for i in s :
            res[c].append(i)
            if t :
                c+=1
            else:
                c-=1
            if c == numRows-1:
                t=False
            if c == 0:
                t =True
        
        res = ["".join(i) for i in res]
        return "".join(res)

