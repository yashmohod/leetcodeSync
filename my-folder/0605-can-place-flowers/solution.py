class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = flowerbed

        if len(f) <=1:
            if (f[0] ==0  and n <=1) or (f[0]==1 and n == 0):
                return True
            else:
                return False

        if f[0] ==0 and f[1] == 0:
            f[0] = 1 
            n-=1
        for i in range(1,len(f)-2):
            if f[i-1] == 0 and f[i+1] == 0 and f[i]==0:
                f[i]=1
                n-=1
            if n ==0:
                return True
        if f[-1] == 0 and f[-2] ==0:
            n-=1
   

        return n < 1 
