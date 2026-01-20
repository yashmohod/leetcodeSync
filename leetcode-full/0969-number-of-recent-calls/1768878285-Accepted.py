class RecentCounter:

    def __init__(self):
        self.counter = []

    def ping(self, t: int) -> int:
        self.counter.append(t)
        count = -1
        while abs(count) < len(self.counter) and self.counter[count-1]>= t-3000: 
            count -= 1
        return abs(count)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
