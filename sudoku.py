# Sudoku Solver
# The main idea for the solution is using a recursive algorithm that iterates through the empty cell on the board, and on the possible candidate numbers for each empty cell, and tries to fill them, as the following code scheme:

# A helper function that returns a set of all valid
# candidates for a given cell in the board

function getCandidates(board, row, col):
    # For some empty cell board[row][col], what possible
    # characters can be placed into this cell
    # that aren't already placed in the same row,
    # column, and sub-board?
 
    # At the beginning, we don't have any candidates
    candidates = []
    
    # For each character add it to the candidate list
    # only if there's no collision, i.e. that character 
    # doesn't already exist in the same row, column 
    # and sub-board. Notice the top-left corner of (row, col)'s 
    # sub-board is (row - row%3, col - col%3).
    for chr from '1' to '9':
        collision = false;
        for i from 0 to 8:
            if (board[row][i] == chr || 
                board[i][col] == chr ||
                board[(row - row % 3) + floor(i / 3)][(col - col % 3) + i % 3] == chr):
                    collision = true
                    break
                  
        if (!collision):
            candidates.push(chr)
         
    return candidates
 
function sudokuSolve(board):
    # For each empty cell, consider 'newCandidates', the
    # set of possible candidate values that can
    # be placed into that cell.
   
    row = -1 
    col = -1
    candidates = null 
    
    for r from 0 to 8:
        for c from 0 to 8:
            if (board[r][c] == '.'):
                newCandidates = getCandidates(board, r, c)
                # Then, we want to keep the smallest
                # sized 'newCandidates', plus remember the
                # position where it was found
                if (candidates == null OR newCandidates.size() < candidates.size()):
                    candidates = newCandidates
                    row = r 
                    col = c
 
    # If we have not found any empty cell, then
    # the whole board is filled already
    if (candidates == null):
        return true
 
    # For each possible value that can be placed
    # in position (row, col), let's
    # place that value and then recursively query
    # whether the board can be solved.  If it can,
    # we are done. 
    for val in candidates:
        board[row][col] = val
        if (sudokuSolve(board)):
            return true
        # The tried value val didn't work so restore  
        # the (row, col) cell back to '.'
        board[row][col] = '.'
 
    # Otherwise, there is no value that can be placed
    # into position (row, col) to make the
    # board solved
    return false
While there are many ways to improve these results even more, make sure your peer has a reasonable sudoku solver at the end of the interview. Usually, the interviewer prefers a working code which isn’t optimal, over a failed attempt for an optimal function.
