class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        rooms = []
        intervals.sort()
        count = 0
        for i in intervals:
            heappush(rooms,i[1])
            while(i[0] >= rooms[0]):
                heappop(rooms)
            count = max(len(rooms),count)
        
        return count

        
        
