class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        ans = []
        def back(dep,sum,comb):

            if dep == k and sum == n and comb not in ans :
                print(comb)
                ans.append(comb)
            else:
                for i in range(10):
                    temp = comb.copy()
                    temp.append(i)
                    back(dep+1,sum+i,temp)

        for i in range(10):
            back(0,i,[i])
        
        print(ans)

        return ans

