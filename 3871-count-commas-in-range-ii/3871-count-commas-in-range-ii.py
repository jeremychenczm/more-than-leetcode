class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        d = 1  # 表示几位数，初始化为1

        # 0-9, 10-99, 100-999, 1000-9999, 10000-99999, ... 依次迭代计算
        while True:
            # 当前位数的最小值，比如d=4时，最小值为1000
            mn = 10 ** (d - 1)
            if mn > n:
                break
            mx = min(10 ** d - 1, n)
            cnt = mx - mn + 1
            ans += cnt * ((d - 1) // 3)
            d += 1

        return ans