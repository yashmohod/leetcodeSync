class Solution:
    def reverse(self, x: int) -> int:
        s = x//abs(x)
        x//=s
        print(x)
        x = str(x)
        r = [i for i in x[::-1]]
        r = int("".join(r))

        if r > 2**(32)-1 or r < -2**32:
            return 0
        else:
            return s * r

