# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        def binSea(start:int,end:int,arr:List[int]):


            cur = round((start + end)/2)
            print(cur,arr[cur],guess(arr[cur]) )

            if guess(arr[cur]) < 0 :
                return binSea(start,cur,arr)
            if guess(arr[cur]) > 0 :
                return binSea(cur,end,arr)
            if guess(arr[cur]) == 0 :
                return arr[cur]            
        temp = list(range(1,n+1))
        print(temp)
        return binSea(0,n-1,temp)
