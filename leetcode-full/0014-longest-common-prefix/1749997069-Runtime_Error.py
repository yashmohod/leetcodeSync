class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        

        ans = ""

        for i in range(len(strs[0])):
            for j in strs:
                if i == len(s) or s[j] != strs[0][i]:
                    return ans
            ans =+ i 

        return ans
