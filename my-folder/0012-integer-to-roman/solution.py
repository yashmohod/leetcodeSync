class Solution:
    def intToRoman(self, num: int) -> str:
        num = str(num)
        num = [int(i) for i in num[::-1]]
        res=[]

        sol = [
            ["I","V"],
            ["X","L"],
            ["C","D"],
            ["M"," "],
        ]

        for i in range(len(num)):
            if num[i] <=3:
                res += [sol[i][0]]*num[i]
            elif num[i] == 4:
                res.append(sol[i][1]+sol[i][0])
            elif num[i] == 5:
                res.append(sol[i][1])
            elif num[i]>5 and num[i]<9:
                res += [sol[i][0]]*(num[i] - 5)
                res.append(sol[i][1])
            elif num[i] == 9:

                res.append(sol[i+1][0]+sol[i][0])


        res = "".join(res)
        res = res[::-1]
        return res


        


