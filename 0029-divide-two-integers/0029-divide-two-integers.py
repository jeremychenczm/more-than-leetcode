class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        neg = (dividend < 0) != (divisor < 0)

        dvd, dvs = abs(dividend), abs(divisor)

        ans = 0
        while dvd >= dvs:
            tmp, mul = dvs, 1
            # 倍增
            while dvd >= (tmp << 1):
                tmp <<= 1
                mul <<= 1
            dvd -= tmp
            ans += mul
        
        return -ans if neg else ans