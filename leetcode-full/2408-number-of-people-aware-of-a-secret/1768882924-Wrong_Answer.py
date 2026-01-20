class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:


        q = deque([1])
        
        for i in range(n):
            tmp = deque([])
            
            while q :
                cur = q.pop() 
                if cur > delay and cur <= forget:
                    tmp.append(0)
                tmp.append(cur+1)
            print(i+1,len(tmp),tmp)
            q = tmp

        return len(q)% ((10**9)+7)


