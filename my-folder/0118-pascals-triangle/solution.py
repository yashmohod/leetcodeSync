class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans =[[1]]
        for i in range(numRows-1):
            cur = [1]
            for j in range(len(ans[-1])-1):
                cur.append(ans[-1][j] +ans[-1][j+1])
            cur.append(1)
            ans.append(cur)
        # print(ans)

        return ans
