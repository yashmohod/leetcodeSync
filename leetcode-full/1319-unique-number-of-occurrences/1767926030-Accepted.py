class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occ = {}

        for i in arr:
            occ[i] = occ.get(i,0)+1

        has = set([])
        for x,y in occ.items():
            if y in has:
                return False
            has.add(y)
        return True
