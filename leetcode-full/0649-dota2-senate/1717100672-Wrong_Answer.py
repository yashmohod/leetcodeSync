class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = deque(list(senate))
        cur=senate[0]
        count=0
        courtInSession=True
        while courtInSession:
            if "D" not in senate or "R" not in senate or len(senate)==1:
                break
            i = senate.popleft()
            if cur ==i :
                count+=1
                senate.append(i)
            elif cur !=i  and count >0:
                count-=1
            elif count ==0:
                cur=i
                senate.pop()
                senate.append(i)
            print(senate)
        if senate[0] =="R":
            return "Radiant"
        if senate[0] =="D":
            return "Dire"

