class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        ans = 0
        n = len(img1)
        for dx in range(-(n - 1), n):
            for dy in range(-(n - 1), n):
                cnt = 0
                for i in range(n):
                    for j in range(n):
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n:
                            cnt += img1[i][j] * img2[ni][nj]
                ans = max(ans, cnt)

        return ans