class Solution:
    def isUgly(self, n: int) -> bool:
        n = abs(n)
        def isPrime(nm):
            f=[]
            for i in range(2,nm):
                if nm % i == 0:
                    f.append(i)

            return len(f) == 0
        if n >= 7:
            for i in range(7,n):
                if isPrime(i) and n%i == 0:
                    return False

        if n==1 or n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
            return True
