class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        min1 = min2 = inf
        max1 = max2 = max3 = -inf

        for x in nums:
            # 维护最小值和次小值
            if x < min1:
                min2 = min1
                min1 = x
            elif x < min2:
                min2 = x

            # 维护前三大
            if x > max1:
                max3 = max2
                max2 = max1
                max1 = x
            elif x > max2:
                max3 = max2
                max2 = x
            elif x > max3:
                max3 = x

        return max(max1 * max2 * max3, min1 * min2 * max1)