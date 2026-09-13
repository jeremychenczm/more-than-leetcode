class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for ac in accounts:
            w = sum(ac)
            ans = max(ans, w)
        return ans