class StockSpanner:

    def __init__(self):

        self.a = []
        

    def next(self, price: int) -> int:
        
        self.a.append(price)
        r = 0 
        n = len(self.a)-1
        while 0<=n and self.a[n]<= price:
            r+=1
            n-=1
        return r


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
