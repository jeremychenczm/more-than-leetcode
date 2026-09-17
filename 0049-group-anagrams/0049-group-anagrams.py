class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = defaultdict(list)
        for s in strs:
            cnt = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                cnt[idx] += 1
            ans[tuple(cnt)].append(s)
        
        return list(ans.values())