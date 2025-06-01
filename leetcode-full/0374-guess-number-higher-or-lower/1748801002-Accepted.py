# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l=0
        r=n-1
        c=round((r+l)/2)

        gr = guess(c+1)
        while gr !=0:
            print(c,c+1,gr)
            if r-l ==1:
                if guess(l+1)==0:
                    return l+1
                if guess(r+1)==0:
                    return r+1

            if gr <0:
                r=c
            if gr >0:
                l=c
            c=round((r+l)/2)
            gr = guess(c+1)
        
        if gr == 0:
                return c+1
        
