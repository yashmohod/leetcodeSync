class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        ans = []
        products.sort()
        word = ""
        for i in searchWord:
            cur =[]
            word +=i
            for j in products:
                if word in j:
                    cur.append(j)
            if len(cur)>3:
                cur = cur[:3]
            ans.append(cur)
        
        return ans 

