class Solution:
    def equalFrequency(self, word: str) -> bool:
        
        aw = {}

        for i in word:
            if i in aw:
                aw[i]+= 1
            else:
                aw[i] =1

        aa = []
        for key, value in aw.items():
            aa.append(value)
        count = 0
        fi = aa[0]
        for i in aa:
            count += i %fi
        
        if count > 1:
            return False
        else:
            return True
