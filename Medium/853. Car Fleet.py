class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position,speed))
        lastCarTime = -math.inf
        counter = 0
        
        for i in range(len(position)-1,-1,-1):
            curr_time = (target-cars[i][0])/cars[i][1]
            if lastCarTime < curr_time:
                lastCarTime = curr_time
                counter += 1
                
        return counter
