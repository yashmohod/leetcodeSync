class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        

        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]
        count=0
        for start,end in intervals[1:]:

            prevEnd = output[-1][1]

            if start < prevEnd:
                # output[-1][1] = max(prevEnd,end)
                count+=1
            else:
                output.append([start,end])
        
        return count 
