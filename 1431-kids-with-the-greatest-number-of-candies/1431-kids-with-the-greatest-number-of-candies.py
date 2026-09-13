class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        cur_max = max(candies)
        ans = [False] * len(candies)
        for i in range(len(candies)):
            if extraCandies + candies[i] >= cur_max:
                ans[i] = True
        return ans