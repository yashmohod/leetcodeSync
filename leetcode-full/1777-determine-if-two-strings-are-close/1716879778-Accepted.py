class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1=Counter(word1)
        w2=Counter(word2)

        print(set(list(w1)),set(list(w2)),set(list(w1))==set(list(w2)))
        if set(list(w1)) == set(list(w2)):
            print(Counter(w1.values()),Counter(w2.values()),Counter(w1.values())==Counter(w2.values()))
            if Counter(w1.values()) == Counter(w2.values()):
                return True
        return False
