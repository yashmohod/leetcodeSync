class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans =[]
        size = len(intervals)
        intervals.sort()
        skip = False
        for i in range(size-1):
            if intervals[i][1]>= intervals[i+1][0]:
                min_ = min(intervals[i][0],intervals[i][1],intervals[i+1][1],intervals[i+1][0])
                max_ = max(intervals[i][0],intervals[i][1],intervals[i+1][1],intervals[i+1][0])
                ans.append([min_,max_])
                skip = True
            else:
                # print(intervals[i])
                if not skip:
                    ans.append(intervals[i])
                else:
                    skip = False
        if not skip:
            ans.append(intervals[-1])
        return ans
        
