class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suffix_min = [0] * n
        cur_min = float('inf')
        for i in range(n - 1, -1, -1):
            cur_min = min(cur_min, nums[i])
            suffix_min[i] = cur_min

        cur_max = -1
        for i, num in enumerate(nums):
            cur_max = max(cur_max, num)
            if cur_max - suffix_min[i] <= k:
                return i
        return -1 