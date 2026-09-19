from collections import deque
class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if n == 1:
            return grid[0][0]

        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def can_reach(t):
            if grid[0][0] > t:
                return False
            visited = [[False] * n for _ in range(n)]
            visited[0][0] = True

            q = deque([(0, 0)])
            while q:
                x, y = q.popleft()
                if x == n - 1 and y == n - 1:
                    return True
                for dx, dy in DIRS:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] <= t:
                        visited[nx][ny] = True
                        q.append((nx, ny))
            return False

        l, r = 0, n * n - 1
        while l < r:
            mid = (l + r) // 2
            if can_reach(mid):
                r = mid
            else:
                l = mid + 1
        return l