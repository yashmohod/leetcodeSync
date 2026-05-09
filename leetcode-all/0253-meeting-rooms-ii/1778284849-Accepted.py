class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        rooms = []
        intervals.sort()

        for i in intervals:
            if len(rooms)==0:
                rooms.append([i])
            else:
                cont = False
                for j in rooms:
                    if j[-1][1] <= i[0]:
                        j.append(i)
                        cont = True
                        break
                if not cont: 
                    rooms.append([i])
        return len(rooms)

        
        
