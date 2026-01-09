class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        o1 = {}
        o2 = {}

        for i in word1:
            o1[i] = o1.get(i,0) +1 
        for i in word2:
            o2[i] = o2.get(i,0) +1

        return set(o1.values())  == set(o2.values())  and set(o1.keys()) == set(o2.keys())
        
           
