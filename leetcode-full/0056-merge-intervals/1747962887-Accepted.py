class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        size = len(intervals)
        if size <2:
            return intervals
        intervals.sort()

        overlapCheck =[]
        curMax = intervals[0]
        for i in range(size):
            if curMax[1] < intervals[i][0]:
                overlapCheck.append(False)
                curMax = intervals[i]
            elif (curMax[1] >= intervals[i][0] and
                  curMax[1] <= intervals[i][1]):
                  overlapCheck.append(True)
                  curMax = intervals[i]
            elif curMax[1] > intervals[i][1]:
                overlapCheck.append(True)
            
        # print(overlapCheck)
        toMerge=[]
        cur=[]
        for i in range(size):
            if overlapCheck[i]:
                cur.append(intervals[i])
            else:
                toMerge.append(cur)
                cur =[intervals[i]]
            # if i == size-1:
                
        if overlapCheck[-1]:
            cur.append(intervals[-1])
            toMerge.append(cur)
        else:
            toMerge.append([intervals[-1]])

        print(toMerge)
        ans=[]
        for i in toMerge:
            all =[]
            for j in i:
                all = list(set(all).union(j))

            ans.append([min(all),max(all)])
        return ans

                


 

        
