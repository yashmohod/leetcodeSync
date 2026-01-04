class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        v = set(['a','e','i','o','u']) 

        count = 0
        res = count
        for i in range(len(s)):
            count += 1 if s[i] in v else 0
            count -= 1 if i >= k and s[i-k] in v else 0
            res = max(res,count) 
        return res
