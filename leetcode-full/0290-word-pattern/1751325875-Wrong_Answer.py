class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        p = list(pattern)
        s = s.split(" ")
        po = {}

        for i in range(len(p)):
            if p[i] in po:
                if po[p[i]] != s[i]:
                    return False
            else:
                po[p[i]] = s[i]
        
        return True
