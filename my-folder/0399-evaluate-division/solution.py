class Solution:
    def calcEquation(self, equations, values, queries):
        g = {}

        for (x, y), ans in zip(equations, values):
            g.setdefault(x, []).append((y, ans))
            g.setdefault(y, []).append((x, 1.0 / ans))

        def dfs(cur, des, seen):
            if cur == des:
                return 1.0

            for nxt, w in g[cur]:
                if nxt in seen:
                    continue
                seen.add(nxt)
                sub = dfs(nxt, des, seen)
                if sub != -1.0:
                    return w * sub
            return -1.0

        res = []
        for cur, des in queries:
            if cur not in g or des not in g:
                res.append(-1.0)
            else:
                res.append(dfs(cur, des, set([cur])))
        return res

