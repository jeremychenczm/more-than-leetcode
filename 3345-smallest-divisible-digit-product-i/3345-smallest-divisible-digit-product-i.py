class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while prod(int(d) for d in str(n)) % t:
            n += 1
        return n