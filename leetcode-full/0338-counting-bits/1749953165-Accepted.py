class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]

        if n == 0 :
            return ans
        if n >= 1 :
            ans.append(1)
        if n == 2:
            ans.append(1)
            return ans
        
        for i in range(2,n+1):
            if i %2 > 0 :
               ans.append( ans[-1]+1)
            else:
                som = 0 
                j = i 
                while j>1:
                    if j%2>1:
                        som+=1
                    j= j/2
                som +=1
                ans.append(som)

        return ans
