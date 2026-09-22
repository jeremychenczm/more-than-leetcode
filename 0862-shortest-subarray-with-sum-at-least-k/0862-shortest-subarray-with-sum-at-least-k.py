from collections import deque
class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        # 暴力解就是对每一个元素为起点进行枚举，达到sum >= k时更新已知的最短subarray长度
        # 通过暴力可知重复的操作在于终点固定时，两个不一样的起点都要对当前之后的元素重新sum一遍
        # 所以想到用前缀和来进行快速查询？

        # 以上方法还是超时了，进一步优化，观察到同样是固定end，我们希望找到更靠右的start
        # 那么当 i<j 且 prefix[i] >= prefix[j] >= k，那么i就可以丢弃了，因为起点j更靠右
        # 所以这里可以用单调递增的双端队列，以此来踢掉更早但更大的前缀

        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        ans = n + 1
        dq = deque()
        
        for j in range(n + 1):
            # subarr_sum = prefix[j] - prefix[i]
            while dq and prefix[j] - prefix[dq[0]] >= k:
                ans = min(ans, j - dq.popleft())
            while dq and prefix[j] <= prefix[dq[-1]]:
                dq.pop()
            dq.append(j)

        return ans if ans <= n else -1