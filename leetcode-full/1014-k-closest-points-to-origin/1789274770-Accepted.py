class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def dis(a):
            return (a[0]**2 + a[1]**2)**(0.5)

        r = [[dis(x),x] for x in points ]
        r.sort()
        
        res = []
        for i in range(k):
            res.append(r[i][1])
        return res
