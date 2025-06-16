class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        print(digits)
        n = len(digits)-1
        carry = 0
        for i in range(n+1):
            print(digits[n-i])
            cur = digits[n-i]+1+carry
            carry = cur// 10
            digits[n-i] = cur %10
            if carry == 0 :
                break
        if carry >0 :
            digits = [carry]+ digits

        return digits
