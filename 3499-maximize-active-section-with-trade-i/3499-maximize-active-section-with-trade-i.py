class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        # 1 0 1 0 1

        t = '1' + s + '1'
        n = len(t)

        # 游程编码，将线性字符串或数组分隔成k组，这样保证的是每一组 至少 交替都是不同的
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
        for i in range(1, k - 1):
            if segs[i][0] == '1':
                # 当前段是'1'，那么左右两段一定是不同的，也就是'0'
                cnt = group_len[i - 1] + group_len[i + 1]
                ans = max(ans, base + cnt)

        return ans