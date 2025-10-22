class Solution:
    def reverseWords(self, s: str) -> str:
        
        words=s.split()

        ans=""
        for i in range(len(words)):
            if words[-i-1] != " " or words[-i-1]!="":
              ans= ans+words[-i-1]+" "
        return ans[:-1]
