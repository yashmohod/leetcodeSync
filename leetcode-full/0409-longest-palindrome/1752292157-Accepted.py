class Solution:
    def longestPalindrome(self, s: str) -> int:
        mp = {}
        for i in s :
            mp[i] = mp[i]+1 if i in mp else 1 
        longest = 0
        center = False
        for x,y in mp.items():
            print(x,y)

            if y == 1 and not center:
                longest +=y 
                center = True

            if y%2 == 0 :
                longest +=y
            else:
                if not center:
                    longest += y
                    center = True
                else:
                    longest += y - 1
            
            print(longest)
        return longest 
