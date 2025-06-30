class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        prev = [nums[0]]
        ans = []
        for i in nums[1:]:
            if prev[-1]+1 == i:
                prev.append(i)
            else:

                if len(prev) == 1:
                    ans.append(str(prev[0]))
                else:
                    ans.append(str(prev[0])+"->"+str(i))
                # ans.append(prev)
                prev = [i]
        if len(prev) == 1:
            ans.append(str(prev[0]))
        else:
            ans.append(str(prev[0])+"->"+str(i))
        # print(ans)

        return ans

