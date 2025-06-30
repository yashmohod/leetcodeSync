class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        

        count =0

        while n  >= 2**count:
            print(n,2**count)
            if n == 2**count:
                return True
            count += 1

        return False
