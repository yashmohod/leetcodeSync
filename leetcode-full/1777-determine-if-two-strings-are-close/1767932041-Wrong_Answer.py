class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if len(word1) != len(word2):
            return False
             
        o1 = {}
        o2 = {}

        for i in word1:
            o1[i] = o1.get(i,0) +1 
        for i in word2:
            o2[i] = o2.get(i,0) +1

        ll = set(o1.values()) 
        rr = set(o2.values()) 

        return ll == rr
        
           
