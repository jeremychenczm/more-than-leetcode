class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        l_max = r_max = 0
        ans = 0
        
        while l < r:
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])
            if l_max <= r_max:
                ans += l_max - height[l]
                l += 1
            else:
                ans += r_max - height[r]
                r -= 1
        
        return ans