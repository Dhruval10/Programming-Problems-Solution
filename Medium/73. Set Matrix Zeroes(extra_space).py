class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = set()
        column = set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    column.add(j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row or j in column:
                    matrix[i][j] = 0
