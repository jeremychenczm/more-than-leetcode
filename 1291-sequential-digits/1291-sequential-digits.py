class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        # 通过案例可以想到本质上就是在数字'123456789'上截取子串
        # len(low) <= len(subarr) <= len(high)
        m, n = len(str(low)), len(str(high))
        S = '123456789'
        ans = []
        # 滑动窗口截取
        for window_len in range(m, n + 1):
            for i in range(10 - window_len):
                cur = int(S[i:i+window_len])
                if low <= cur <= high:
                    ans.append(cur)

        return ans