class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # 把两个变量控制成一个
        # values[i] + i + values[j] - j
        ans = mx = 0  # mx -> max(values[i] + i)
        for j, val in enumerate(values):
            ans = max(ans, mx + val - j)
            mx = max(mx, val + j)
        return ans