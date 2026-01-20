class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        d = 0
        r = 0

        for i in senate:
            if i == "R":
                r+=1
                d-=1
            if i == "D":
                d+=1
                r-=1
        print(d,r)
        if d > r:
            return "Dire"
        elif r > d:
            return "Radiant"
        else:
            if senate[0]== "R":
                return "Radiant"
            else:
                return "Dire"

