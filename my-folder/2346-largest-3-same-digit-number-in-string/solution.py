class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        ans = ""
        # print(len(num)-2)

        for i in range(len(num)-2):
            # print( num[i],num[i+1],num[i+2])
            if num[i] == num[i+1] and num[i] == num[i+2]:
                if ans == "":
                    ans = num[i]+num[i+1]+num[i+2]
                else:
                    cur = num[i]+num[i+1]+num[i+2]

                    for i in range(3):
                        if int(cur[i]) > int(ans[i]):
                            ans = cur
                            break
                        
        
        return ans 
