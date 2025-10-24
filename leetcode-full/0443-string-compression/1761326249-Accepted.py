class Solution:
    def compress(self, chars: List[str]) -> int:
        
        f=0
        c=chars[0]
        res=""
        for i in chars:
            # print(f,c,i)
            if i == c:
                f+=1
            else:
                res+=c
                if f>1:
                    res+=str(f)
                f=1
                c=i
        res+=c
        if f>1:
            res+=str(f)
        f=1
        c=i
        # print(res)

        for i,j in enumerate(res):
            chars[i]=j
        
        return len(res)
