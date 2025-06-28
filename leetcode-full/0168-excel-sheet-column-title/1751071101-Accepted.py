class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        base26 = []

        while columnNumber > 0 :
            columnNumber -= 1
            # print(columnNumber,columnNumber//26,columnNumber%26)
            base26.append(columnNumber%26)
            columnNumber = columnNumber//26
        base26.reverse()
        # print(base26)
        ans = ""

        for i in base26:
            ans += chr(i+65)

        return ans 
