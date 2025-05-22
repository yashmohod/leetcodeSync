class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans =[]
        size = len(intervals)
        skip = False
        for i in range(size-1):
            if intervals[i][1]>= intervals[i+1][0]:
                ans.append([intervals[i][0],intervals[i+1][1]])
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
        
