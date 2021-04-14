class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        return (moves.count('L') == moves.count('R')) & (moves.count('U') == moves.count('D'))
