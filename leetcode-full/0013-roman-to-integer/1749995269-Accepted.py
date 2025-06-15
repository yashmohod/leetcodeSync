class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0 
        # rk = {
        #         "I":1,
        #         "V":5,
        #         "X":10,
        #         "L":50,
        #         "C":100,
        #         "D":500,
        #         "M":1000}
        ansTab = dict()
        s = s[::-1]
        for i in s :

            if i == "V":
                print(5)
                ans +=5
                ansTab["V"] =1

            if i == "L":
                print(50)
                ans +=50
                ansTab["L"] =1

            if i == "D":
                print(500)
                ans +=500
                ansTab["D"] =1

            if i == "M":
                print(1000)
                ans +=1000
                ansTab["M"] =1

            if i == "I":
                if "V" in ansTab or "X" in ansTab:
                    print(-1)
                    ans-=1
                else:
                    print(1)
                    ans+=1
                    ansTab["I"] =1

            if i == "X":
                if "L" in ansTab or "C" in ansTab:
                    print(-10)
                    ans-=10
                else:
                    print(10)
                    ans+=10
                    ansTab["X"] =1

            if i == "C":
                if "D" in ansTab or "M" in ansTab:
                    print(-100)
                    ans-=100
                else:
                    print(100)
                    ans+=100
                    ansTab["C"] =1

        return ans
            
            
                
            


            
            
            


