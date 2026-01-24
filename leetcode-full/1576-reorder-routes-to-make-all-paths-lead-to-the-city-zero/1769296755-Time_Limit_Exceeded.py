class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        graph = {city:[] for city in range(n)}
        self.count = 0
        seen = set()
        for a,b in connections:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(cur):
                for efrom in graph[cur]:
                    if efrom in seen:
                        continue
                    if [efrom,cur] not in connections:
                        self.count+=1
                    seen.add(efrom)    
                    dfs(efrom)
        seen.add(0)
        dfs(0)
        return self.count



