class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.total = 0
        self.array = []

    def next(self, val: int) -> float:
        self.array.append(val)
        if len(self.array) > self.size:
            self.total -= self.array[0]
            self.array = self.array[1:]

        self.total = self.total + val
        
        return (self.total)/len(self.array)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
