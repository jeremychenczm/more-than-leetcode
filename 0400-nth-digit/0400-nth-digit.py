class Solution:
    def findNthDigit(self, n: int) -> int:
        # 1- 9 = 9， 10 - 99 = 90 * 2， 100 - 999 = 900 * 3 ...
        # 9 * 1, 90 * 2, 900 * 3, 9000 * 4, ...
        # 9 * 10^(k - 1) * k

        digits = 1
        count = 9
        start = 1
        while n > digits * count:
            n -= digits * count
            digits += 1
            count *= 10
            start *= 10
        
        num = start + (n - 1) // digits
        idx = (n - 1) % digits
        return int(str(num)[idx])