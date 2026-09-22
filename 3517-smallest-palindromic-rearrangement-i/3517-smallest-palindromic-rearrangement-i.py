class Solution:
    def smallestPalindrome(self, s: str) -> str:
        """
        原本就是回文串，直接取一半字母进行重排序，镜像构造就好
        """
        n = len(s)
        half_len = n // 2  # 向下取整
        # 计算左半段字母的频次便于完整构造
        count = [0] * 26
        for ch in s[:half_len]:  # 此时右开区间，也就是奇数时那个字符是没有构造进去的
            count[ord(ch) - ord('a')] += 1
        left_chars = []
        for i in range(26):
            left_chars.append(chr(ord('a') + i) * count[i])
        left = ''.join(left_chars)

        # 构造镜像右半段
        right = left[::-1]
        # 如果是奇数，
        if n % 2 == 1:
            mid = s[half_len]
            return left + mid + right
        return left + right