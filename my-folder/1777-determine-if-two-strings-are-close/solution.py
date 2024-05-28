class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1=Counter(word1)
        w2=Counter(word2)
        return set(list(w1)) == set(list(w2)) and Counter(w1.values()) == Counter(w2.values())
