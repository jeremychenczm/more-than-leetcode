from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_cnt = defaultdict(int)
        prefix_cnt[0] = 1
        ans = total = 0
        for i, num in enumerate(nums):
            total += num
            target = total - k
            if target in prefix_cnt:
                ans += prefix_cnt[target]
            prefix_cnt[total] += 1
        return ans