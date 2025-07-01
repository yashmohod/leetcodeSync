class Solution:
    def equalFrequency(self, word: str) -> bool:
        
        def cf(s):
            d={}

            for i in s:
                if i in d:
                    d[i]+=1
                else:
                    d[i] = 1
            
            dd ={}
            for i in d.values():
                dd[i] =1
            
            if len(dd.values()) == 1:
                return True
            else:
                return False

        for i in range(len(word)):
            if cf(word[:i] +word[i+1:]):
                return True

        return False
            
            

        
