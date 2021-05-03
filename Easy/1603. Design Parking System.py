class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.bigger = big
        self.smaller = small
        self.mediums = medium

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.bigger>0:
                self.bigger -= 1
                return True
            else:
                return False
        if carType == 2:
            if self.mediums>0:
                self.mediums -= 1
                return True                
            else:
                return False
        if carType == 3:
            if self.smaller>0:
                self.smaller -= 1
                return True
            else:
                return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
