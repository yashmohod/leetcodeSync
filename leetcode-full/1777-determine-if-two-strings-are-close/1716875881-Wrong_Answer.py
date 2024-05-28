class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return len(set(Counter(word1).values())) == len(set(Counter(word2).values()))
