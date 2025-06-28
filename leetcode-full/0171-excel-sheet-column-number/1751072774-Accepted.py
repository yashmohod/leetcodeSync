class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        

        count =len(columnTitle)-1
        ans = 0
        for i in columnTitle:
            # print((ord(i)-64),count)
            ans += (ord(i)-64)* 26**count
            count-=1
        
        return ans
