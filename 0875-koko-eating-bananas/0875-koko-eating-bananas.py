class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # eat all but with minimum k within h hours
        # slowly, so: 1 <= k <= max(piles)

        def can_finish(speed):
            hours = 0
            for p in piles:
                hours += (p + speed - 1) // speed
            return True if hours <= h else False

        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            if can_finish(mid):
                r = mid
            else:
                l = mid + 1
        return l