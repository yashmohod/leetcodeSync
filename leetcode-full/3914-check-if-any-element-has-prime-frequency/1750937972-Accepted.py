import numpy as np
class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:

        def isPrime(n):
            if n  == 1:
                return False
            factors = []

            for i in range(2,int(np.sqrt(n))+1):
                if n%i == 0 :
                    factors.append(i)

            if len(factors)>0:
                return False
            else:
                return True
                

        freq = {}

        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i] = 1

        for x,y in freq.items():
            if isPrime(y):
                return True

        return False
