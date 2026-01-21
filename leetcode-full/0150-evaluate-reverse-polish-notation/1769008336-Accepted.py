class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        q = deque([])

        for i in tokens:
            if i == "+":
                b = q.pop()
                a = q.pop()
                q.append(a+b)
            elif i == "-":
                b = q.pop()
                a = q.pop()
                q.append(a-b)
            elif i == "*":
                b = q.pop()
                a = q.pop()
                q.append(a*b)
            elif i == "/":
                b = q.pop()
                a = q.pop()
                q.append(int(a/b))
            else:
                q.append(int(i))
        
        return q[0]
