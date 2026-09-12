class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        # total = 4k(k + 1)
        k, remain = divmod(n, 8)
        total = 4 * k * (k + 1)
        total += remain * (k + 1)
        return total

        
        