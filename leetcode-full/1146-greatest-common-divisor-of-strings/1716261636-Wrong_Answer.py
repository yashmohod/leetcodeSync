class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        ans=""
        if str1[0] != str2[0]:
            return ans
        else:
            str1len = len(str1)
            str2len = len(str2)
            anslen = 0
            if str1len>str2len:
                anslen = str1len/str2len
            else:
                anslen = str2len/str1len
            iftrue = True

            for i in range(anslen):
                if str1[i] != str2[i]:
                    iftrue = False
            
            if iftrue:
                return str1[0:anslen+1]


        
