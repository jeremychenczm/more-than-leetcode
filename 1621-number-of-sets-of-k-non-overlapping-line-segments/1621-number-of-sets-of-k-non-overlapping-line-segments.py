class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 1_000_000_007
        return comb(n + k - 1, k * 2) % MOD