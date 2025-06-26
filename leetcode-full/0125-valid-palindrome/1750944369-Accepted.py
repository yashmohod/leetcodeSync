class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()

        ans =""
        print(s)
        for i in s:
            if (ord(i) >=97 and  ord(i) <= 122) or (ord(i) >=48 and  ord(i) <= 57):
                ans +=i
        print(ans)
        for i in range(len(ans)//2):
            if ans[i] != ans[-i-1]:
                return False
        return True
