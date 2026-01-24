class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        def dfs(key,visited):
            if key not in visited:
                visited.add(key)
                for i in rooms[key]:
                    dfs(i,visited)
            
        visited = set()
        dfs(0,visited)
        print(visited)
        return len(visited) == len(rooms)
