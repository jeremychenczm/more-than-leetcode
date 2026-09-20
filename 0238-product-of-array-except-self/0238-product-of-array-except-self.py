class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [1] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i - 1] * nums[i - 1]

        suffix = 1    
        for j in range(n, 0, -1):
            ans[j] = ans[j - 1] * suffix
            suffix *= nums[j - 1]
        
        return ans[1:]