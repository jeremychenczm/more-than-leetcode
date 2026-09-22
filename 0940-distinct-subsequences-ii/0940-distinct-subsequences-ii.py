class Solution:
    def distinctSubseqII(self, s: str) -> int:
        """
        如果当前字符 c 之前从没出现过，那么加上它会让子序列总数直接翻倍——因为原来每个子序列都可以选择"加 c"或"不加 c"。但如果 c 之前出现过，翻倍就会产生重复，而这部分重复恰好等于"上一次出现 c 之前"那个时刻的子序列总数。只要维护一个"当前为止的子序列总数（含空序列）"，每来一个新字符就翻倍再减去它上次出现前的旧总数，就能不生成任何子序列、直接算出计数。
        """
        MOD = 1_000_000_007
        total = 1
        last = {}
        for c in s:
            new_total = (2 * total - last.get(c, 0)) % MOD
            last[c] = total
            total = new_total
        return (total - 1) % MOD  # 减去一个空序列
