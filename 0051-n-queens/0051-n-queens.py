class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        self.ans = []
        self.n = n
        queens = [-1] * n
        self.bt(queens, 0)
        return self.ans

    def bt(self, queens, row_idx):
        # 每行都设置好皇后
        if row_idx == self.n:
            self.ans.append(self.build(queens))
            return
        
        # 放置皇后
        for col_idx in range(self.n):
            if self.isvalid(queens, row_idx, col_idx):
                queens[row_idx] = col_idx
                self.bt(queens, row_idx + 1)  # 放置下一行
                queens[row_idx] = -1  # 回溯
        
    
    def isvalid(self, queens, row_idx, col_idx):
        for i in range(row_idx):
            if queens[i] == col_idx:
                return False
            if abs(row_idx - i) == abs(col_idx - queens[i]):
                return False
        return True

    
    def build(self, queens):
        board = []
        for i in range(self.n):
            row_arr = ["."] * self.n
            row_arr[queens[i]] = "Q"
            board.append(''.join(row_arr))
        return board
