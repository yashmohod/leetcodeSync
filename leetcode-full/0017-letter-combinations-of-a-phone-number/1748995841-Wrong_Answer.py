class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        letters = [[],[],["abc"],["def"],["ghi"],["jkl"],["mno"],["pqrs"],["tuv"],["wxyz"]]
        answer = []


        def rec(digs, comb):

            if digs == "":
                answer.append(comb)
            else:
                
                for i in letters[int(digs[0])]:
                    print(comb+i)
                    rec(digs[1:],comb+i)

        rec(digits,"")
        print(answer)

        return answer


        
