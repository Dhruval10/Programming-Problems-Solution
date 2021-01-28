class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        tempColor = image[sr][sc]
        
        if tempColor == newColor:
            return image
        
        def changeColor(image, row, column, newColor, tempColor):
            if row < 0 or column < 0 or row >= len(image) or column >= len(image[0]) or image[row][column] != tempColor:
                return 
            image[row][column] = newColor
            
            if row > 0:
                changeColor(image, row-1, column, newColor, tempColor)
            if column > 0:
                changeColor(image, row, column-1, newColor, tempColor)
            if row < len(image):
                changeColor(image, row+1, column, newColor, tempColor)
            if column < len(image[0]):
                changeColor(image, row, column+1, newColor, tempColor)
            # return image
        
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] == tempColor:
                    changeColor(image, sr, sc, newColor, tempColor)
                    

        return image