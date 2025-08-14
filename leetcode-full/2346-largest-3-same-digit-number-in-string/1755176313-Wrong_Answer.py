class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        ans = ""

        for i in range(len(num)-3):
            if num[i] == num[i+1] and num[i] == num[i+2]:
                if ans == "":
                    ans = num[i]+num[i+1]+num[i+2]
                else:
                    ans = str(max(int(ans),int(num[i]+num[i+1]+num[i+2])))
        
        return ans 
