class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = [product.lower() for product in products]
        products.sort()
        results=[]
        for i in range(1,len(searchWord)+1):
            print(searchWord[:i])
            result = []
            count = 0
            while(len(result)<3 and count <len(products) ):
                if(products[count].startswith(searchWord[:i]) ):
                    result.append(products[count])
                count +=1
            results.append(result)
        print(results)
        return results

