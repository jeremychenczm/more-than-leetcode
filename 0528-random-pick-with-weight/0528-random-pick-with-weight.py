class Solution:
    """
    把输入的权重拍平到数轴上，比如[2, 1, 4], 那么分割点就是[2, 3, 7]
    也就是[0, 2], [2, 3], [3, 7]这几段区间，数字[0, 7]落到区间的概率刚好是前缀和
    """
    def __init__(self, w: list[int]):
        self.split_point = []
        total = 0
        for weight in w:
            total += weight
            self.split_point.append(total)
        self.total_sum = total

    def pickIndex(self) -> int:
        target = random.randint(1, self.total_sum)
        return bisect_left(self.split_point, target)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()