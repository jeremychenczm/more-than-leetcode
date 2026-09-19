class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2 ** 31 - 1
        is_neg = x < 0
        x = abs(x)

        num = 0
        while x > 0:
            digit = x % 10
            x //= 10
            if num > INT_MAX // 10 or (num == INT_MAX // 10 and digit > 7):
                return 0
            num = num * 10 + digit

        return -num if is_neg else num