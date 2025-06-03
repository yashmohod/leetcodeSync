class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # print("H = ",h)
        def hours( k, p):
            a=0
            for i in p:
                # print(i//k,i%k)
                if i%k > 0 :
                    a += i//k +1
                else:
                    a += i//k
            # print("A = ",a)
            return a

        l = 1
        r = max(piles)
        
        while l < r:
            
            m = (l+r)//2
            print(m,l,r)
            if hours(m,piles) > h :
                l = m +1
            else:
                r -=1
               
        
        return l
