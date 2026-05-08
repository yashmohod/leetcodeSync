class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) < 2:
            return True

        intervals.sort()

        for i in range(1,len(intervals)):
            a = intervals[i-1] 
            b = intervals[i]

            if (a[0] >= b[0] and a[0] <= b[1]) or (b[0] >= a[0] and b[0] <= a[1]):
                return False

        return True 
