class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        q = deque([])

        for i in tokens:
            if i == "+":
                b = q.pop()
                a = q.pop()
                print(a,i,b)
                q.append(a+b)
            elif i == "-":
                b = q.pop()
                a = q.pop()
                print(a,i,b)
                q.append(a-b)
            elif i == "*":
                b = q.pop()
                a = q.pop()
                print(a,i,b)
                q.append(a*b)
            elif i == "/":
                b = q.pop()
                a = q.pop()
                print(a,i,b,int(a/b))
                q.append(int(a/b))
            else:
                q.append(int(i))
        
        return q[0]
