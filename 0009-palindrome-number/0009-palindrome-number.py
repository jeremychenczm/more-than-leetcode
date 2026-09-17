class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        p1, p2 = 0 , len(num) - 1
        while p1 < p2:
            if num[p1] != num[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True