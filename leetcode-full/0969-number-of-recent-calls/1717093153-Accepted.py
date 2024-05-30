class RecentCounter:

    def __init__(self):
        self.reqs=[]


    def ping(self, t: int) -> int:
        self.reqs.append(t)
        counter=0
        for i in self.reqs:
            if i < t-3000:
                counter+=1
            else:
                break

        return len(self.reqs[counter:])


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
