class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # print(digits)
        n = len(digits)-1
        # print("n",n)
        carry = 0
        for i in range(n+1):
            # print(digits[n-i])
            cur = digits[n-i]+carry
            if i == 0 :
                cur +=1

            carry = cur// 10
            # print(carry,i)
            digits[n-i] = cur %10
            if carry == 0 :
                break
        print(carry)
        if carry >0 :
            digits = [carry]+ digits

        return digits
