class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """找起点才不会超时"""
        ans = 0
        nums_set = set(nums)
        for num in nums_set:
            # 有更小的说明当前num不是起点
            if num - 1 in nums_set:
                continue
            end = num
            while end + 1 in nums_set:
                end += 1
            ans = max(ans, end - num + 1)
        return ans