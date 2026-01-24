class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        def dfs(key):
            cur = rooms[key]

            if -1 in cur:
                return 
            else:
                rooms[key].append(-1)
                for i in cur:
                    dfs(i)
        dfs(0)
        for i in rooms:
            if -1 not in i:
                return False
        return True
