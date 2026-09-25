class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        # 1 0 1 0 1

        t = '1' + s + '1'
        n = len(t)

        # 游程编码，将线性字符串或数组分隔成k组
        # 这里每一组记录(字符， 长度)
        segs = []
        i = 0
        while i < n:
            j = i
            while j < n and t[j] == t[i]:
                j += 1
            segs.append([t[i], j - i])
            i = j

        # t预加了两个1，头尾两组长度需要 -1， 
        group_len = [length for _, length in segs]
        group_len[0] -= 1
        group_len[-1] -= 1

        base = s.count('1')
        ans = base
        k = len(segs)
        for i in range(2, k - 2):
            if segs[i][0] == '1':
                cnt = group_len[i - 1] + group_len[i + 1]
                ans = max(ans, base + cnt)

        return ans