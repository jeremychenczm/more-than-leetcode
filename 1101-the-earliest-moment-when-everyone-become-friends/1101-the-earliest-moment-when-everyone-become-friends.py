class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        parent = list(range(n))
        rank = [0] * n
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra

            if rank[ra] == rank[rb]:
                rank[ra] += 1
            return True

        logs.sort(key=lambda log: log[0])
        remaining = n
        for ts, a, b in logs:
            if union(a, b):
                remaining -= 1
                if remaining == 1:
                    return ts

        return -1