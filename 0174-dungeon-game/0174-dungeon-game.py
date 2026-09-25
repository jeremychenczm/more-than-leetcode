class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])

        # dp[i][j]：站在 (i, j) 这一格，进入这一格之前至少需要多少血量，
        # 才能保证从这里出发一路走到终点，且全程血量 > 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                dp[i][j] = float('inf')

        # 再往前一步就是终点，至少需要留 1 点血
        dp[m - 1][n] = 1
        dp[m][n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    need = 1
                else:
                    need = min(dp[i + 1][j], dp[i][j + 1])
                # 进入 (i,j) 前需要的血量 = 走完这格之后至少还剩 need，
                # 反推回来进入前需要 need - dungeon[i][j]，且至少是 1
                dp[i][j] = max(1, need - dungeon[i][j])

        return dp[0][0]