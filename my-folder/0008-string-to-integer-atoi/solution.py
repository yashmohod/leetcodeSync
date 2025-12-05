class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s)==0:
            return 0
        l=0
        while l<len(s) and s[l]==" ":
            l+=1
        s = s[l:] if l>0 else s
        res =[]
        opt ="1234567890"
        sig ="-+"
        curSig ="+"    
        print(s)
        for i,j in enumerate(s):
            if j in opt:
                res.append(j)
            else:
                if i ==0:
                    if j in sig:
                        curSig =j
                    else:
                        return 0
                else:
                    break
        # print(res)
        if len(res)==0:
            return 0
        res = int("".join(res))
        res = res  if curSig =="+" else -res
        # print(res)
        if res > 2**31 -1:
            return 2**31 -1
        elif res < -2**31 :
            return -2**31
        else:
            return res




