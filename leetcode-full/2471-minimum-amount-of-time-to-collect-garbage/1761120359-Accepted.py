class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        som = 0
        G=0
        P=0
        M=0
        ps = 0 
        for i in range(len(garbage)):
            som += len(garbage[i])
            if i > 0 :
                ps +=travel[i-1]
                if "G" in garbage[i]:
                    G= ps
                if "P" in garbage[i]:
                    P= ps
                if "M" in garbage[i]:
                    M= ps
        
        return som+G+P+M
