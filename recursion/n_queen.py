def solveNQueens(n):
    res = []
    col = set()
    pos_diog = set()
    neg_diog = set()

    board = [["."]*n for _ in range(n)]

    def backtrack(r):
        if r == n:
            copy_b = ["".join(row) for row in board]
            res.append(copy_b)
            return
        
        for c in range(n):
            if c in col or (r+c) in pos_diog or (r-c) in neg_diog:
                continue

            col.add(c)
            pos_diog.add(r+c)
            neg_diog.add(r-c)
            board[r][c] = "Q"

            backtrack(r+1)

            col.remove(c)
            pos_diog.remove(r+c)
            neg_diog.remove(r-c)
            board[r][c] = "."
    
    backtrack(0)
    return res

print(solveNQueens(4))
