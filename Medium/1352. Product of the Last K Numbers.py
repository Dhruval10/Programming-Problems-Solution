class ProductOfNumbers:
    def __init__(self):
        self.array = []
        self.multiplyer = 1

    def add(self, num: int) -> None:
        if num != 0:
            self.multiplyer *= num
            self.array.append(self.multiplyer)
        else:
            self.multiplyer = 1
            self.array = []

    def getProduct(self, k: int) -> int:
        if len(self.array) < k:
            return 0
        if len(self.array) == k:
            return self.array[-1]
        else:
            return self.array[-1]//self.array[-1-k]
        
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
