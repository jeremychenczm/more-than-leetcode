class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0

        # 数战舰的起点就好，因为不相邻，所以它的起点左边和上边一定没有'X'
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c == 'X' and (j == 0 or row[j - 1] != 'X') and (i == 0 or board[i - 1][j] != 'X'):
                    ans += 1
        return ans
