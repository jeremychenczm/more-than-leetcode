class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        suf = [-1] * (m + 1)
        suf[m] = n
        i = n - 1
        for j in range(m - 1, -1, -1):
            while i >= 0 and word1[i] != word2[j]:
                i -= 1
            if i < 0:
                break
            suf[j] = i
            i -= 1

        ans = []
        changed = False
        j = 0
        for i in range(n):
            if j == m:
                break
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            elif not changed and suf[j + 1] != - 1 and suf[j + 1] > i:
                ans.append(i)
                j += 1
                changed = True
        
        return ans if j == m else []