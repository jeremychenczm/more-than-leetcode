class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cur_sum = nums[0]
        ans = nums[0]

        # 要嘛连续累加要嘛从当前元素为起点开始计算
        for num in nums[1:]:
            cur_sum = max(num, cur_sum + num)
            ans = max(ans, cur_sum)

        return ans