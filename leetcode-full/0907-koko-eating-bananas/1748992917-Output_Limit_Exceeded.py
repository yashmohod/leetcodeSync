class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        print("H = ",h)
        def hours( k, p):
            a=0
            for i in p:
                print(i//k,i%k)
                if i%k > 0 :
                    a += i//k +1
                else:
                    a += i//k
            print("A = ",a)
            return a

        z = 1
        print("Z = ",z)
        while hours( z, piles) > h :
            z +=1
            print("Z = ",z)

    

        return z
