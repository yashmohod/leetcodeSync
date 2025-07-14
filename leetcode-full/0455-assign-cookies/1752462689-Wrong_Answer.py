class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0 
        for i in s:
            print(i in g,len(g) )
            if len(g) <= 0 :
                return count
            
            if i in g :
                count +=1
                g.remove(i)
        
        return count 
