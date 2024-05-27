class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        p=0
        if s =="":
            return True

        for i in t:
            if i == s[p]:
                p+=1
        
        if p == len(s):
            return True
        else:
            return False
