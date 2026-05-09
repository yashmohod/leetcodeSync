class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = {}

        for i in strs:
            c = list(i)
            c.sort()
            c ="".join(c)
            if c in res :
                res[c].append(i)
            else:
                res[c] = [i]
        return list(res.values())
