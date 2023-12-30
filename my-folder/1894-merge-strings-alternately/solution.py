class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        mergeResult=""
        for i in range(len(word1)+ len(word2)):
            
            if i >= len(word1) or i >= len(word2):
                if i >= len(word2):
                    mergeResult = mergeResult + word1[i:]
                if i >= len(word1):
                    mergeResult = mergeResult + word2[i:]
                break
            else:
                mergeResult = mergeResult+ word1[i]+word2[i]  
        return mergeResult

        
