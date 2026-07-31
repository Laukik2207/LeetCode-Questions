class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        self.queue.append(t)
        x = 0
        for i in self.queue:
            if(i >= t-3000 and i <= t):
                x+=1
        return x


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)