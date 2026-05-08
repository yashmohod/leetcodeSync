class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        count = 0
        start,end = 0,0

        for i in intervals:
            start = min(start,i[0])
            end = max(end,i[1])
        
        for i in range(start,end+1):
            cc = 0
            for j in intervals:
                if j[0] <= i < j[1]:
                    cc+=1
            count = max(cc,count)
        return count

        
        
