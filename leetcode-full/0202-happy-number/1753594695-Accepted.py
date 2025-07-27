class Solution:
    def isHappy(self, n: int) -> bool:
        

        def some(num):
            s = 0
            while num > 0 :
                r = num%10
                s += r*r
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
