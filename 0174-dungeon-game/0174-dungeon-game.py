class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        # 我首先想到候选答案是升序的，[1, total_neg]
        # 尝试用答案二分

        m, n = len(dungeon), len(dungeon[0])

        def canRescue(start_health: int) -> bool:
            # dp[i][j]：以 start_health 出发，走到 (i, j) 时能保有的最大血量
            # -1 表示这个格子在血量 > 0 的前提下不可达
            dp = [[-1] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i == 0 and j == 0:
                        h = start_health + dungeon[i][j]
                    else:
                        best_prev = -1
                        if i > 0 and dp[i - 1][j] > 0:
                            best_prev = max(best_prev, dp[i - 1][j])
                        if j > 0 and dp[i][j - 1] > 0:
                            best_prev = max(best_prev, dp[i][j - 1])
                        if best_prev <= 0:
                            continue
                        h = best_prev + dungeon[i][j]
                    if h > 0:
                        dp[i][j] = h
            return dp[m - 1][n - 1] > 0

        neg_total = 0
        for row in dungeon:
            for v in row:
                if v < 0:
                    neg_total += v

        l, r = 1, max(1, abs(neg_total) + 1)
        while l < r:
            mid = (l + r) // 2
            if canRescue(mid):
                r = mid
            else:
                l = mid + 1
        return l