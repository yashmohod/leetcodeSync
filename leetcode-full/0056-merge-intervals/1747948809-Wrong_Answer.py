class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        overlapCheck =[]
        size = len(intervals)
        if size <2:
            return intervals
        intervals.sort()
        # print(intervals)
        skip = False
        for i in range(size-1):
            if intervals[i][1] >= intervals[i+1][0]:
                overlapCheck.append(True)
            else:
                overlapCheck.append(False)

        mergeQ=[]
        cur=[]
        print(len(overlapCheck),size)
        for i in range(size-1):
            if overlapCheck[i]:
                cur.append(intervals[i])
            else:
                cur.append(intervals[i])
                mergeQ.append(cur)
                cur = []
        if overlapCheck[-1]:
            cur.append(intervals[-1])
            mergeQ.append(cur)
        else:
            mergeQ.append([intervals[-1]])

        ans = []
        for i in mergeQ:
            min_ = min(i[0][0],i[0][1],i[-1][0],i[-1][1])
            max_ = max(i[0][0],i[0][1],i[-1][0],i[-1][1])
            ans.append([min_,max_])
        return ans
        
