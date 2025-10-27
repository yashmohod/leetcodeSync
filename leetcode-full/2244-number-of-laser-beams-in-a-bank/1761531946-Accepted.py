class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        f =[]

        for i in bank:
            c=0
            for j in i:
                if j == "1":
                    c+=1
            f.append(c)
        
        b=0
        l,r=0,0
        while r<len(f):
            while l<len(f) and f[l]==0 :
                l+=1
            r=l+1
            while r<len(f) and f[r]==0:
                r+=1
            if r < len(f):
                b += f[l]*f[r]
                l+=1
                r+=1
        print(f)

        return b

