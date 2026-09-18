class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        l = r = 0
        st = []
        ans = []
        while r < len(nums):
            if not st or st[-1] < nums[r]:
                st.append(nums[r])
            if r - l + 1 == k:
                ans.append(st[-1])
                l += 1
            r += 1
        return ans