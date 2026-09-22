class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        # dp[idx][M] 表示：石堆还剩下从下标 idx 到末尾，当前允许的上限是 M，能拿到的最多石子
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for idx in range(n - 1, -1, -1):
            for M in range(n, 0, -1):
                # 如果剩余的石子数量小于当前上限，那么全拿了
                if idx + 2 * M >= n:
                    dp[idx][M] = suffix[idx]
                # 否则按规则枚举X，找出最优选项
                else:
                    best = 0
                    for X in range(1, 2 * M + 1):
                        # 求在选择拿X之后，产生的新M是多少
                        new_M = min(M if M > X else X, n)
                        # 总石子数量 - 对手通过新状态拿到的石子数量 = 自己当前拿的
                        best = max(best, suffix[idx] - dp[idx + X][new_M])
                    dp[idx][M] = best

        return dp[0][1]