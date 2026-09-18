class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 栈里存的是"当前还没被匹配上的字符的下标"，
        # 栈顶到当前位置的距离，正好就是一段连续合法括号的长度
        # 比如 (()(())) -> (  (())) -> (  (  )) -> (      )

        st = [-1]
        ans = 0
        for i, c in enumerate(s):
            if c == '(':
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    ans = max(ans, i - st[-1])

        return ans
