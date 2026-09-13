class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = Counter(digits)
        ans = 0

        # 常熟可能，直接暴力枚举
        for num in range(100, 1000, 2):
            high, mid, low = num // 100, (num // 10) % 10, num % 10
            need = Counter([high, mid, low])  # 计算每一个数所需的频次
            # 验证是否能满足
            if all(freq[digit] >= cnt for digit, cnt in need.items()):
                ans += 1
        
        return ans