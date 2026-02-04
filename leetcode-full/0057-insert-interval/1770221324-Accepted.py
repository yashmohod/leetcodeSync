class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals.sort()
        res = []
        prev = intervals[0]

        for x,y in intervals:
            if prev[1] >=x:
                mi = min([x,y,prev[0],prev[1]])
                ma = max([x,y,prev[0],prev[1]])
                prev = [mi,ma]
            else:
                res.append(prev)
                prev = [x,y]
        res.append(prev)
        return res
