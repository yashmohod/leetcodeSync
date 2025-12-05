class Solution:
    def reverse(self, x: int) -> int:
        if x ==0:
            return 0
        s = x//abs(x)
        x//=s
        print(x)
        x = str(x)
        r = [i for i in x[::-1]]
        r = int("".join(r))
        print((2**(32))-1,-(2)**32)
        if r > (2**(32))-1 or r < -(2)**32:
            return 0
        else:
            return s * r

