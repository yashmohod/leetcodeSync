class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) < 2:
            return True

        intervals.sort()

        for i in range(1,len(intervals)):
            a = intervals[i-1] 
            b = intervals[i]

            if b[0] < a[1]:
                return False

        return True 
