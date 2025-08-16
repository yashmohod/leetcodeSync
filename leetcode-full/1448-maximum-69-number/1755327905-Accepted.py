class Solution:
    def maximum69Number (self, num: int) -> int:
        
        c = num
        num = str(num)
        for i in range(len(num)):
            s = 9 if num[i] == 6 else 9
            c = max(int(num[:i]+str(s)+num[i+1:]),c)

        return c
