class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = cnt = 0
        for num in nums:
            if num == 1:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 0
                
        return max(ans, cnt)