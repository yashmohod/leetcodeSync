class StockSpanner:

    def __init__(self):

        self.a = []
        

    def next(self, price: int) -> int:

        s = 1
        while self.a and self.a[-1][0] <= price:
            s+= self.a.pop()[1]

        self.a.append([price,s])
        return s  

# obj = StockSpanner()
# param_1 = obj.next(price)
