class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = float('-inf')

        # map保存某个num值对应的最小前缀值
        # 因为固定某个nums[j]，我们要找的是当 
        # nums[j] + k || nums[j] - k = nums[i] = target 的最小子数组sum，
        # sum = prefix[j] - prefix[i]
        # 所以问题转换为 key=target 的最小的前缀
        num_minPrefix = {}
        prefix = 0
        
        for j in range(n):
            cur = nums[j]

            # target = cur - k || cur + k
            # cur + prefix - prefix[target] = total
            if cur - k in num_minPrefix:
                ans = max(ans, prefix + cur - num_minPrefix[cur - k])
            if cur + k in num_minPrefix:
                ans = max(ans, prefix + cur - num_minPrefix[cur + k])

            if cur not in num_minPrefix or num_minPrefix[cur] > prefix:
                num_minPrefix[cur] = prefix
            
            prefix += cur

        return ans if ans != float('-inf') else 0