class Solution:
    def partitionString(self, s: str) -> int:
        

        ht = {}
        count = 1

        for i in s:
            # print(i,ht)
            if i in ht:
                count +=1 
                ht = {}
            ht[i]=1
        
        return count
