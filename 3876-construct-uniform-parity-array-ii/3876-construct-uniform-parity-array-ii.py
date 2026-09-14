class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odds = [x for x in nums1 if x % 2]
        if not odds:
            return True
        min_odd = min(odds)
        return all(x > min_odd for x in nums1 if x % 2 == 0)
