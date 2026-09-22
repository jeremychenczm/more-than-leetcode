class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        """
        首先，每一个字母都必然能找到它的第一次出现位置和最后一次出现位置，那么就得到了一个初步的区间。
        但是，在这个区间里可能又会有其他字母，如果产生了区间重叠，比如a[0, 3], b[2, 5]，那么此时就要相对应的把a区间的右端点扩大到b的右端点，就有a[0, 5], b[2, 5]，以此类推更复杂情况

        最终，我们会得到一个固定区间结果，且只有包含与不相交两种情况，不会有区间段重叠的情况，因为之前已经动态扩张修改过区间定位。

        基于以上结果，将区间按照右端点排序，从索引0开始遍历所有区间，比如a[0, 5] b[2, 4]，那么当然贪心的选小不选大，然后从端点5开始继续向右选择其他区间

        """

        n = len(s)

        # 1.遍历所有字母（各自）的左右区间端点
        left = [-1] * 26
        right = [-1] * 26
        for c_idx, c in enumerate(s):
            idx = ord(c) - ord('a')
            if left[idx] == -1:  # 没出现过就是左端点
                left[idx] = c_idx
            right[idx] = c_idx    # 否则就更新右端点


        candidates = []
        # 2.对区间内其他字母出现时动态更新右端点进行闭包
        for c_idx, c in enumerate(s):
            idx = ord(c) - ord('a')

            # 如果不是左端点就跳过
            if left[idx] != c_idx:
                continue

            new_right = right[idx]
            ptr = c_idx
            valid = True
            # 在当前左端点对应的区间内动态更新
            while ptr <= new_right:
                other_c = ord(s[ptr]) - ord('a')

                # 如果区间内部遇到的字母左端点是比当前区间还靠左的，那么就无法包含它
                # 当前字母的区间也无法继续动态更新，因为无法闭包，直接退出循环
                if left[other_c] < c_idx:
                    valid = False
                    break
                new_right = max(new_right, right[other_c])
                ptr += 1

            if valid:
                candidates.append((c_idx, new_right))


        # 3.区间右端点排序贪心选择
        candidates.sort(key=lambda x:x[1])
        ans = []
        last_end = -1
        for start, end in candidates:
            if start > last_end:
                ans.append(s[start:end+1])
                last_end = end

        return ans

                
            