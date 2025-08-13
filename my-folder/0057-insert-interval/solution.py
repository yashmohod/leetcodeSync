class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # print(newInterval)
        # print(intervals)
        intervals = intervals + [newInterval]
        # print(intervals)
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        for start,end in intervals[1:]:

            prevEnd = output[-1][1]

            if start <= prevEnd:
                output[-1][1] = max(prevEnd,end)
            else:
                output.append([start,end])
        
        return output 
