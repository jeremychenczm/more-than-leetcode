class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # after split, largest sum is minimized
        # so, max(nums) <= ans <= sum(nums)

        def can_split(target):
            cnt = 1
            total = 0
            for num in nums:
                if total + num > target:
                    total = 0
                    cnt += 1
                total += num
            return cnt <= k

        l, r = max(nums), sum(nums)
        while l < r:
            mid = (l + r) // 2
            if can_split(mid):
                r = mid
            else:
                l = mid + 1
        return l