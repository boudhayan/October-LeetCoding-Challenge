class RecentCounter:

    def __init__(self):
        self.requests = []

# Time Complexity: O(n)
# Space Complexity: O(1)
    def ping(self, t: int) -> int:
        # add new request to the requests list
        self.requests.append(t)
        # filter out all the requests whose timestamp is t - 3000
        while self.requests[0] < t - 3000:
            self.requests = self.requests[1:]
        # return current number of requests in the requests list after filtering completed
        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
