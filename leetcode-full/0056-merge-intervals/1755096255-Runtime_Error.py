class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        interval.sort(key = lambda i : i[0])
        output = [interval[0]]

        for start,end in interval[1:]:

            prevEnd = output[-1][1]

            if start <= prevEnd:
                output[-1][1] = max(prevEnd,end)
            else:
                output.append([start,end])
        
        return output 
