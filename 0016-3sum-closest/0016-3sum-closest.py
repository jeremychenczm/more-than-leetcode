class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        # ans is closet to target
        sorted_arr = sorted(nums)
        n = len(nums)

        diff = float('inf')
        for i, num in enumerate(sorted_arr):
            l, r = i + 1, n - 1
            while l < r:
                total = sorted_arr[l] + sorted_arr[r] + sorted_arr[i]
                if abs(target - total) < abs(diff):
                    diff = target - total
                if total < target:
                    l += 1
                else:
                    r -= 1
            
            if diff == 0:
                break
        
        return target - diff
