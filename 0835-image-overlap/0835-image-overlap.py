from collections import defaultdict
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        A = [(i, j) for i in range(n) for j in range(n) if img1[i][j] == 1]
        B = [(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1]

        if not A or not B:
            return 0

        cnt = defaultdict(int)
        for ai, aj in A:
            for bi, bj in B:
                offset = (bi - ai, bj - aj)
                cnt[offset] += 1

        return max(cnt.values())