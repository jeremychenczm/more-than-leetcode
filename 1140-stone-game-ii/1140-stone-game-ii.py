class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for idx in range(n - 1, -1, -1):
            for M in range(n, 0, -1):
                if idx + 2 * M >= n:
                    dp[idx][M] = suffix[idx]
                else:
                    best = 0
                    for X in range(1, 2 * M + 1):
                        new_M = min(M if M > X else X, n)
                        best = max(best, suffix[idx] - dp[idx + X][new_M])
                    dp[idx][M] = best

        return dp[0][1]