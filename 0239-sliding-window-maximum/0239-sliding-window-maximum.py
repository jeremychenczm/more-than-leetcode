from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()
        ans = []
        n = len(nums)

        for i in range(n):
            # 先查队列头部元素是否超出窗口
            if dq and dq[0] <= i - k:
                dq.popleft()
            # 维护单调递增队列
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                ans.append(nums[dq[0]])
        
        return ans