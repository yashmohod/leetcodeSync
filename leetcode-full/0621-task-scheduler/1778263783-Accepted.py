class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        td = {}
        for i in tasks:
            td[i] = td.get(i,0)+1
        hp = []
        for i in td.values():
            heappush(hp,-i)
        q = deque([])
        time = 0
        while hp or q:
            time +=1

            if hp:
                cur = heappop(hp) +1
                if cur != 0:
                    q.append([cur,time+n])
            
            if q and q[0][1] == time:
                cur,_ = q.popleft()
                heappush(hp,cur)
        
        return time



        
