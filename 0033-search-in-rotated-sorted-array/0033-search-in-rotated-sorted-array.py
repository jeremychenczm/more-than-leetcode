class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if nums[mid] < nums[0]:
        # says it was in rotated subarray

        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            # 左半[l, mid]有序
            if nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # 右半[mid, r]有序
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1