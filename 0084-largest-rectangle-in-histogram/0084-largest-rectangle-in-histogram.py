class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 从左往右观察到，一旦元素开始递减，那么说明相邻左侧元素遇到右边界，可以开始结算
        # 由此推出要维护一个单调递增序列，然后不断弹栈结算栈内元素
        st = []
        n = len(heights)
        ans = -1

        for i in range(n + 1):
            # cur_h作为比较元素，来确认栈内元素是否要结算
            h = 0 if i == n else heights[i]
            while st and h < heights[st[-1]]:
                cur_idx = st.pop()
                left_bound = st[-1] if st else -1
                right_bound = i
                area = (right_bound - left_bound - 1) * heights[cur_idx]
                ans = max(ans, area)
            
            st.append(i)

        return ans