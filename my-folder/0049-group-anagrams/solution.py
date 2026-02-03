class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r = {}
        for i in strs:
            s = list(i)
            s.sort()
            s="".join(s)
            if s in r:
                r[s].append(i)
            else:
                r[s]=[i]
        return list(r.values())
