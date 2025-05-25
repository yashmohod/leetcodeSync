class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        q = deque()

        for n in nums:
            if q :
                t = q.pop()
                o = deque()
                o.append(t)
                if t > n :
                    while t> n and q:
                        t = q.pop()
                        o.append(t)
                    add = True
                    while o:
                        tmp  = o.pop()
                        if tmp > n and add:
                            q.append(n)
                            add = False
                        q.append(tmp)
                else:
                    o.pop()
                    q.append(t)
                    q.append(n)
            else:
                q.append(n)
        
        while q :
            tmp = q.pop()
            if k == 1 :
                return tmp 
            k -=1



