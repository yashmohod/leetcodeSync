class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        def dfs(key):
            cur = rooms[key]

            if len(cur)==0:
                return 
            else:
                rooms[key] = []
                for i in cur:
                    dfs(i)
        dfs(0)
        for i in rooms:
            if len(i)>0:
                return False
        return True
