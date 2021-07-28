class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        # check if astr < 0 and stack[-1] > 0 --> pop all the elements less than abs(astr[i])
        # if astr > 0, add it into the stack
        # if astr[i] < 0 amnd stack[-1] < 0 then add astr[i] into the stack        

        # -8 -8 -8
        stack = []
        
        for i in range(len(asteroids)):
            while stack and asteroids[i] < 0 < stack[-1]:
                # print(abs(asteroids[i]),stack[-1])
                if stack[-1] < -asteroids[i]:
                    stack.pop()
                    continue
                elif stack[-1] == -asteroids[i]:
                    stack.pop()
                break
            else:
                stack.append(asteroids[i])
        
        return stack
