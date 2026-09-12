class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) == 2:
            return True

        n = len(arr)
        mn, mx = min(arr), max(arr)
        if (mx - mn) % (n - 1) != 0:
            return False
        d = (mx - mn) // (n - 1)
        if d == 0:
            return True

        seen = [False] * len(arr)
        for num in arr:
            if (num - mn) % d != 0:
                return False
            idx = (num - mn) // d
            if seen[idx]:
                return False
            seen[idx] = True

        return True
            