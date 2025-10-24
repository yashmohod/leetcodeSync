class Solution:
    def compress(self, chars: List[str]) -> int:
        
        f=0
        c=chars[0]
        ci=0
        res=""
        for i in chars:
            # print(f,c,i)
            if i == c:
                f+=1
            else:
                res+=c
                chars[ci]=c
                ci+=1
                if f>1:
                    fs = str(f)
                    res+=fs
                    for j in fs:
                        chars[ci] =j
                        ci+=1
                f=1
                c=i
        res+=c
        chars[ci]=c
        ci+=1
        if f>1:
            fs = str(f)
            res+=fs
            for j in fs:
                chars[ci] =j
                ci+=1

        # for i,j in enumerate(res):
        #     chars[i]=j
        
        return ci
