class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        f =[]

        for i in bank:
            c=0
            for j in i:
                if j == "1":
                    c+=1
            f.append(c)
        
        while 0 in f:
            f.remove(0)
        
        b = 0
        for i in range(len(f)-1):
            b+=f[i]*f[i+1]
        print(f)

        return b

