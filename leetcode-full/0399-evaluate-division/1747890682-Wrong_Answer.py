class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ans =[]
        for q in queries:
            c1 = False
            c2 = False

            for e in equations:
                if(q[0] == e[0] or q[0] == e[1]):
                    c1=True
                if(q[1] == e[0] or q[1] == e[1]):
                    c2=True
            
            if c1 and c2:
                if q[0] == q[1] :
                    ans.append(1)
                else:
                    notSkip = True
                    for e in equations:
                        if q[0] == e[0] and q[1] == e[1]:
                            ans.append(values[equations.index(e)])
                            notSkip = False
                        if q[0] == e[1] and q[1] == e[0]:
                            ans.append(1/values[equations.index(e)])
                            notSkip = False
                    if notSkip:
                        adjList = collections.defaultdict(list)
                        for e in equations:
                            ab = values[equations.index(e)]
                            adjList[e[0]].append((e[1],ab))
                            adjList[e[1]].append((e[0],1/ab))


                        que=collections.deque()
                        que.append(q[0])
                        done=[q[0]]
                        cost = 1
                        while(len(que)>0):
                            now =  que.popleft()
                            for v,c in adjList[now]:
                                if not (v in done):
                                    done.append(v)
                                    cost =cost *c
                                    que.append(v)
                        ans.append(cost)
                                
            else:
                ans.append(-1)
            

        return ans
