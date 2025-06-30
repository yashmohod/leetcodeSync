class Solution:
    def isUgly(self, n: int) -> bool:
        
        f= []

        for i in range(2,n):
            if n%i == 0:
                f.append(i)
        if 2 in f:
            f.remove(2)
        if 3 in f:
            f.remove(3)
        if 5 in f:
            f.remove(5)

        print(f)
        return len(f) == 0
