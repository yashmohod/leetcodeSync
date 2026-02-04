class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        ans = []
        intervals.sort()
        for cur in  intervals:
            if len(ans) < 1:
                ans.append(cur)
            else:
                x,y = cur
                a,b = ans[-1]
                if x > b:
                    ans.append(cur)
                else:
                    ans.pop()
                    mi = min([x,y,a,b])
                    ma = max([x,y,a,b])
                    ans.append([mi,ma])
        return ans
