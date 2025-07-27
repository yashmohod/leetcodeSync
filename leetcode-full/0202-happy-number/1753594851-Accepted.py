class Solution:
    def isHappy(self, n: int) -> bool:
        

        def some(num):
            s = 0
            while num > 0 :
                s += (num%10)**2
                num //= 10 
            return s

        slow = n 
        fast = n

        while True:
            slow =  some(slow)
            fast = some(some(fast))

            if fast == slow:
                break 
    
        return slow == 1
