from collections import deque
DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        
        # 1. 收集垃圾的{（(i, j)：id} 和 起点坐标
        startx, starty = -1, -1
        litter_id = {}
        for i in range(m):
            for j in range(n):
                cur = classroom[i][j]
                if cur == 'S':
                    startx, starty = i, j
                elif cur == 'L':
                    litter_id[(i, j)] = len(litter_id)
        if len(litter_id) == 0:
            return 0

        # 垃圾通过比特位来表示，比如5个垃圾收集了其中3个：01011
        full_mask = (1 << len(litter_id)) - 1

        best_energy = [[dict() for _ in range(n)] for _ in range(m)]
        start_mask = 0
        best_energy[startx][starty][start_mask] = energy

        q = deque([(startx, starty, start_mask, energy, 0)])
        while q:
            x, y, mask, cur_e, steps = q.popleft()
            # 剪枝：如果当前的能量cur_e < 还在que里的某个相同状态，那么就不继续下去
            if cur_e < best_energy[x][y].get(mask):
                continue
            
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if classroom[nx][ny] == 'X' or cur_e <= 0:
                    continue
                
                nxt_e = energy if classroom[nx][ny] == 'R' else cur_e - 1

                # 查看是否是垃圾
                new_mask = mask
                if (nx, ny) in litter_id:
                    new_mask |= 1 << litter_id[(nx, ny)]  # 是垃圾就在第id个比特位标记
                if new_mask == full_mask:
                    return steps + 1
                
                # 如果有更好的能量或者当前垃圾状态没入队过的就入队，能量小的就不入队
                if nxt_e > best_energy[nx][ny].get(new_mask, -1):
                    best_energy[nx][ny][new_mask] = nxt_e
                    q.append((nx, ny, new_mask, nxt_e, steps + 1))

        return -1


