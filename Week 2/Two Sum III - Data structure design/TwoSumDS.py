
class TwoSum:

    def __init__(self):
        self.dict = {}

    # Time Complexity: O(1) | insertion in dictionary takes a constant amount of time
    def add(self, number):
        if number in self.dict:
            self.dict[number] = self.dict[number] + 1
        else:
            self.dict[number] = 1

    # Time Complexity: O(N) where N is total number of unique numbes in the DS
    def find(self, value):
        for num in self.dict.keys():
            remaining = value - num
            if remaining != num:
                if remaining in self.dict:
                    return True
            elif self.dict[num] > 1:
                return True
        return False


ts = TwoSum()
ts.add(0)
ts.add(-1)
ts.add(-1)
ts.add(0)
# ts.add(7)

print(ts.find(11))
