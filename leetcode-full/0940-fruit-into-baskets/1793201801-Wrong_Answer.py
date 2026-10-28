class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        
        c = Counter(fruits)

        v = list(c.values())
        v.sort(reverse=True)

        if len(v) == 0:
            return 0
        elif len(v) ==1:
            return v[0]
        else:
            return v[0]+v[1]
