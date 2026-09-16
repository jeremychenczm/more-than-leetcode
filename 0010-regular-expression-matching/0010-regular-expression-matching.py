class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        # dp[i][j] = s前i个字符能不能匹配上p前j个字符
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    zero = dp[i][j - 2]
                    match = p[j - 2] == '.' or p[j - 2] == s[i - 1]
                    one_more = match and dp[i - 1][j]
                    dp[i][j] = zero or one_more
                else:
                    match = p[j - 1] == '.' or p[j - 1] == s[i - 1]
                    dp[i][j] = match and dp[i - 1][j - 1]
                    
        return dp[m][n]