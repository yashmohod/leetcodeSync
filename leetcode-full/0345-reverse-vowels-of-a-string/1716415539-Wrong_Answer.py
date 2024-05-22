class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)
        vow=["a","e","i","o","u"]
        has=[]
        for i in s:
            if i in vow:
                has.append(i)
        count = len(has)-1
        for i in range(len(s)):
            if s[i] in vow:
                s[i] = has[count]
                count-=1
        return "".join(s)
        
