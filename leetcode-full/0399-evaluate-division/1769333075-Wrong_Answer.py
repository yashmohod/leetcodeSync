class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        

        g = {}
        for i in range(len(equations)):

            x,y = equations[i]
            print(x,y)
            ans = values[i]
            
            if x in g:
                g[x].append([y,ans])
            else:
                g[x] = [[y,ans]]

            if y in g:
                g[y].append([x,1/ans])
            else:
                g[y] = [[x,1/ans]]
        print(g)
        def dsf(cur,des,seen):
            r = 1
            for too,val in g[cur]:
                if too not in seen:
                    if too == des:
                        return val
                    else:
                        seen.add(too)
                        r = r * dsf(too,des,seen) *val
            return r
        res = []
        for cur,des in queries:
            if cur in g and des in g:
                if cur == des:
                    res.append(1)
                else:
                    seen = set([cur])
                    res.append(dsf(cur,des,seen))
            else:
                res.append(-1)
        return res
