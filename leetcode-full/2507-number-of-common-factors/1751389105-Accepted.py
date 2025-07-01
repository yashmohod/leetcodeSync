class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        

        s = a if a<b else b

        factors=[]

        for i in range(1,s+1):
            if a%i == 0 and b%i == 0:
                factors.append(i)

        return len(factors)
