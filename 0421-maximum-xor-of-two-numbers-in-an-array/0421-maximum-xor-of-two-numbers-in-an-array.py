class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = mask = 0
        high_bit = max(nums).bit_length() - 1

        for i in range(high_bit, -1, -1):
            mask |= 1 << i  # 前缀掩码1，用来下文截取元素前缀
            new_ans = ans | (1 << i)  # 试探性答案：假设第i位也凑出1
            seen = set()
            for x in nums:
                x &= mask  # 截出前缀
                if new_ans ^ x in seen:  # 说明 x ^ y = new_ans
                    ans = new_ans 
                    break
                seen.add(x)  # 没找到答案，就保留当前遍历到的前缀

        return ans

# |  按位或：    只要有一边是1就是1
# &  按位与：    都是1才是1
# ^  按位异或：  两边不同才是1