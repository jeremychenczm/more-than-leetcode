class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = min(n, 2)

        # 遍历，分情况讨论找结果
        i = 1
        while i < n:
            # 外层循环控制起点 + 更新答案，内层负责找最远距离
            if nums[i - 1] > nums[i]:
                i += 1
                continue

            start = i - 1
            while i < n and nums[i - 1] <= nums[i]:
                i += 1

            # 现在[start, i - 1]这个子数组是非递减的
            # 要让数组更长有三种情况：改nums[start - 1], 改nums[i - 1], 改nums[i]
            
            # 1. 改nums[start - 1]，行程 +1，继续往左延长的可能等同于之前往右加长，不重复计算
            ans = max(ans, i - max(start - 1, 0))
            if i == n:
                break

            # 2. 改nums[i]或者nums[i - 1]
            if i < n - 1 and (nums[i - 1] <= nums[i + 1] or nums[i - 2] <= nums[i] <= nums[i + 1]):
                j = i + 2 # i+1 已经接上了，现在看 i+2 的情况
                while j < n and nums[j - 1] <= nums[j]:
                    j += 1
                ans = max(ans, j - start)
            else:
                ans = max(ans, i - start + 1)

        return ans