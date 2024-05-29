class Solution:
    def removeStars(self, s: str) -> str:
        ans=[]

        for i in s:
            if i =="*":
                ans.pop()
            if i!="*":
                ans.append(i)
        return ''.join(ans)
