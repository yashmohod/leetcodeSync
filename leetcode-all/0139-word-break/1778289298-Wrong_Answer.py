class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = 0

        while l< len(s):
            found = False
            for word in wordDict:
                wordLen = len(word)
                if l+wordLen <= len(s) and s[l:l+wordLen] == word:
                    l = l+wordLen
                    found = True
            if not found:
                return False
        
        return True if l >= len(s) else False
                    

