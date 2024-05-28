class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ans = {}

        for i in arr:
            if str(i) not in ans:
                ans[str(i)] = 1
            else:
                ans[str(i)] += 1
        ocs=[]
        for i in list(ans):
            if ans[i] not in ocs:
                ocs.append(ans[i])
            else:
                return False
        return True                
