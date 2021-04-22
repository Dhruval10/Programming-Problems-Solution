class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list1 = []

    def push(self, val: int) -> None:
        self.list1.append(val)

    def pop(self) -> None:
        self.list1.pop()

    def top(self) -> int:
        return self.list1[-1]

    def getMin(self) -> int:
        mini = min(self.list1)
        return mini


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
