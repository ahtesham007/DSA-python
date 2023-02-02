board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

def solve(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                for ch in range(1,10):
                    if isValid(str(ch),r,c):
                        board[r][c] = str(ch)
                        if solve(board):
                            return True
                        else:
                            board[r][c] = "."
                return False
    
    return True
        
def isValid(c, row, col):
    for i in range(9):
        if board[row][i] == c:
            return False
        
        if board[i][col] == c:
            return False
        
        if board[3*(row//3)+(i//3)][3*(col//3) + (i%3)] == c:
            return False
    
    return True



solve(board)
print(board)