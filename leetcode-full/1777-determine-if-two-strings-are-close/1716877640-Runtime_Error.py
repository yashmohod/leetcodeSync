class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1 = Counter(word1)
        w2 = Counter(word2)

        if len(w1.values()) == len(w2.values()):
            print(w1.values(),w2.values(),set(w1.values()).difference(set(w2.values())),set(w2.values()).difference(set(w1.values())))
            if len(set(list(w1)).difference(set(list(w2))))  == 0 and len(set(list(w2)).difference(set(list(w1))))  == 0:
                if len(set(w1.values()).difference(set(w2.values())))  == 0 and et(w2.values()).difference(set(w1.values())) ==0 :
                    if len(word1) == len(word2):
                        return True
                
        return False

        # return Counter(word1) == Counter(word2)
