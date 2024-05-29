class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans=[]

        for i in asteroids:
            if i > 0:
                ans.append(i)
            else:
                tmp=True
                while tmp and len(ans)>0:
                    cur = ans.pop()
                    if cur < 0:
                        ans.append(cur)
                        break
                    else:
                        if abs(i) < abs(cur):
                            ans.append(cur)
                            tmp=False
                        if abs(i) == abs(cur):
                            tmp=False
                if tmp :
                    ans.append(i)
        return ans
