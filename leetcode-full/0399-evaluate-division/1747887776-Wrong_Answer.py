class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
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
                        if(q[0] == e[0] and q[1] == e[1] ):
                            ans.append(values[equations.index(e)])
                            notSkip = False
                        if(q[0] == e[1] and q[1] == e[0] ):
                            ans.append(1/values[equations.index(e)])
                            notSkip = False
                    if notSkip:
                        for e in equations:
                            ab = values[equations.index(e)]
                            if(q[0] == e[0]):
                                for e2 in equations:
                                    cb = values[equations.index(e2)]
                                    if(q[1] == e2[0] and e[1]==e2[1]):
                                        ans.append(ab*(1/cb))
                                    elif(q[1] == e2[1] and e[1]==e2[0]):
                                        ans.append(ab*cb)
                            elif(q[0] == e[1]):
                                for e2 in equations:
                                    cb = values[equations.index(e2)]
                                    if(q[1] == e2[0] and e[0]==e2[1]):
                                        ans.append((1/ab)*(1/cb))
                                    elif(q[1] == e2[1] and e[0]==e2[0]):
                                        ans.append((1/ab)*cb)
                                
            else:
                ans.append(-1)


        return ans
        
