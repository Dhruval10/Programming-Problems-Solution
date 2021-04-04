class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = []
        # self.answer = []
        self.k = k
    # Inserts an element into the circular queue. Return true if the operation is successful.
    def enQueue(self, value: int) -> bool:
        if len(self.queue) < self.k:
            self.queue.append(value)
            return True
        else:
            return False
    # Deletes an element from the circular queue. Return true if the operation is successful.
    def deQueue(self) -> bool:
        try:
            self.queue.pop(0)
            return True
        except:
            return False
    # Gets the front item from the queue. If the queue is empty, return -1.
    def Front(self) -> int:
        try:
            return self.queue[0]
        except:
            return -1
    # Gets the last item from the queue. If the queue is empty, return -1.
    def Rear(self) -> int:
        try:
            return self.queue[-1]
        except:
            return -1
    # Checks whether the circular queue is empty or not.
    def isEmpty(self) -> bool:
        if len(self.queue) == 0:
            return True
        else:
            return False
    # Checks whether the circular queue is full or not.
    def isFull(self) -> bool:
        if len(self.queue) == self.k:
            return True
        else:
            return False

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
