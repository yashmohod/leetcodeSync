class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        pa=[]
        for i in s:
            if i not in t:
                return False
            else:
                pa.append(t.index(i))
        
        for i in range(len(pa)-1):
            if pa[i]>=pa[i+1]:
                return False

        return True
