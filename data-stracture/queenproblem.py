def init(board, row, col, N):
 for i in range(col):
     if board[row][i] == 1:
         return False
 
 for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
     if board[i][j] == 1:
         return False
 
 for i, j in zip(range(row, N), range(col, -1, -1)):
     if board[i][j] == 1:
         return False
  return True
 
def solve_n_queens_util(board, col, N):
 if col >= N:
     return True
 
 for i in range(N):
     if init(board, i, col, N):
         board[i][col] = 1
         if solve_n_queens_util(board, col + 1, N):
             return True
 
     board[i][col] = 0
 return False
def solve_n_queens(N):
     board = [[0] * N for _ in range(N)]
     if not solve_n_queens_util(board, 0, N):
         print("Solution does not exist")
         return False
 
     print("Solution for {} queens:".format(N))
     for row in board:
         print(" ".join(map(str, row)))
     return True
N = 8
solve_n_queens(N)