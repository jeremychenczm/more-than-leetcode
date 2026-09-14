class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        min_odd = (n, float('inf'))
        odd = False
        for idx, num in enumerate(nums1):
            if num % 2 != 0:
                odd = True
                if num < min_odd[1]:
                    min_odd = (idx, num)

        if not odd:
            return True

        for idx, num in enumerate(nums1):
            if num % 2 == 0 and not (idx != min_odd[0] and num - min_odd[1] >= 1):
                return False
        return True
