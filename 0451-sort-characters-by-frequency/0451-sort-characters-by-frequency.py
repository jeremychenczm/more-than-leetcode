class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        res = [''] * len(s)
        for c in cnt:
            res[cnt[c]-1] += cnt[c] * c
            
        return ''.join(reversed(res))