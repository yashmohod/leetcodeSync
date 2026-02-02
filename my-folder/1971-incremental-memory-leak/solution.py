class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
       
        c = 0
        while memory1 - c >=0 or memory2 - c >=0 :
            if memory1 >= memory2:
                memory1-=c
                c+=1
            else:
                memory2-=c
                c+=1
        return [c,memory1,memory2]
