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
        arr = list(range(1,n+1))
        gr = guess(arr[c])
        while gr !=0:
            print(c,arr[c],gr)
            if r-l ==1:
                if guess(arr[l])==0:
                    return arr[l]
                if guess(arr[r])==0:
                    return arr[r]

            if gr <0:
                r=c
            if gr >0:
                l=c
            c=round((r+l)/2)
            gr = guess(arr[c])
        
        if gr == 0:
                return arr[c]
        
