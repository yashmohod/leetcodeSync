class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        q = deque(list(senate))
        counter = 0
        cur = ""
        while len(q)>1:
            c = q.popleft()
            if cur == "":
                counter=1
                cur = c
                q.append(c)
            elif c == cur:
                counter+=1
                q.append(c)
            elif counter==1:
                counter = 0
                cur=""
            else:
                counter -=1
        
        return "Radiant" if q[0]=="R" else "Dire"
                



