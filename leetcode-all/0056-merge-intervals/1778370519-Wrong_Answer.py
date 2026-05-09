class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()

        res = deque([])

        for cur in intervals:
            if len(res)==0:
                res.append(cur)
            else:
                prev =  res.pop()
                if prev[1] >= cur[0]:
                    res.append([prev[0],cur[1]])
                else:
                    res.append(prev)
                    res.append(cur)
                    
        return list(res)
        
