class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1=Counter(word1)
        w2=Counter(word2)

        print(set(list(w1)),set(list(w2)),set(list(w1))==set(list(w2)))
        if set(list(w1)) == set(list(w2)):
            print(set(w1.values()),set(w2.values()),set(w1.values())==set(w2.values()))
            if w1.values() == w2.values():
                return True
        return False
