class Solution:
    def countAndSay(self, n: int) -> str:
        num = '1'
        for _ in range(n - 1):
            nxt = ""
            start = end = 0
            while start < len(num):
                while end < len(num) and num[start] == num[end]:
                    end += 1
                length = end - start
                nxt += str(length) + num[start]
                start = end
            num = nxt
        
        return num