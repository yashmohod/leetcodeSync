class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        

        def dfs(cur,seen):
            if cur not in seen:
                seen.add(cur)
                for i,isCon in enumerate(isConnected[cur]):
                    if isCon:  
                        dfs(i,seen)

        seen = set()
        count = 0
        for i in range(len(isConnected)):
            if i not in seen:
                dfs(i,seen)
                count+=1
        return count

