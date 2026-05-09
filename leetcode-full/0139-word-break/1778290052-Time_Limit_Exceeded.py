class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def dfs(idx):
            if idx == len(s) :
                return True
            m = False
            for word in wordDict:
                wordLen = len(word)
                if idx+wordLen <= len(s) and s[idx:idx+wordLen] == word:
                    m = m or dfs(idx+wordLen)
            return m
        return dfs(0)




