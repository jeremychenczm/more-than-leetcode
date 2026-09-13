class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # nums = [3,3,7,7,10,11,11]
        # idx  =  0,1,2,3,4, 5, 6

        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                l = mid + 2
            else:
                r = mid
        
        return nums[l]