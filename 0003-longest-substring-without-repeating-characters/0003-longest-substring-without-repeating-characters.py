from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        ans = 0
        cnt = defaultdict(int)
        while r < len(s):
            cnt[s[r]] += 1
            while l <= r and cnt[s[r]] > 1:
                del_c = s[l]
                cnt[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
            r += 1

        return ans