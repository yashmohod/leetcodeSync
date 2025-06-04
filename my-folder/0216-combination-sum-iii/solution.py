class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        ans = []
        def back(dep,sum,comb):

            if dep == k  and  sum == n  :
                comb.sort()
                if comb not in ans:
                    print(comb,sum)
                    ans.append(comb)
            else:
                # print(comb)
                if dep < k:
                    for i in range(1,10):
                        if i not in comb:
                            temp = comb.copy()
                            temp.append(i)
                            back(dep+1,sum+i,temp)

        for i in range(1,10):
            back(1,i,[i])
        
        # for i in ans:
        #     print(i)

        return ans

