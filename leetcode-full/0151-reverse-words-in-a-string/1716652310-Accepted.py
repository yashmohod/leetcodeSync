class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=s.split()

        ans=""
        for i in range(len(words)):
            if words[-i-1] != " " or words[-i-1]!="":
              ans= ans+words[-i-1]+" "
        return ans[:-1]
