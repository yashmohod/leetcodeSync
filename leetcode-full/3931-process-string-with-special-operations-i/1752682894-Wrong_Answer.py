class Solution:
    def processStr(self, s: str) -> str:

        result = ""

        for i in s:

            if i == "*" and len(result)>0:
                result = result[:-1]

            if i =="#":
                result += result

            if i == "%":
                result == result[::-1]

            if ord(i)>= 97 and  ord(i)<= 122:
                result += i


        return result
