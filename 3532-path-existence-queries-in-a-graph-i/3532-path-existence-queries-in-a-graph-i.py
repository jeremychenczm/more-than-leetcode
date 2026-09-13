class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        id = [0] * n  # 每个节点所在连通块的编号
        for i in range(1, n):
            id[i] = id[i - 1]  # 先预设继承上一个连通id
            # 如果不满足连通规则，那么新增一个连通id
            if nums[i] - nums[i - 1] > maxDiff:
                id[i] += 1  

        return [id[u] == id[v] for u, v in queries]