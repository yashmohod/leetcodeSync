class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        c = {}
        def dfs(idx):
            if idx == len(s) :
                return True
            m = False
            for word in wordDict:
                wordLen = len(word)
                if idx+wordLen <= len(s) and s[idx:idx+wordLen] == word: 
                    if not (idx+wordLen in c):
                        c[idx+wordLen] = dfs(idx+wordLen)
                    m = m or c[idx+wordLen]    
            return m
        return dfs(0)




