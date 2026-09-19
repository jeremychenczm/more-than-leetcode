from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        start = end = 0
        n = len(fruits)
        types = defaultdict(int)
        ans = 0

        while end < n:
            types[fruits[end]] += 1
            while len(types) > 2:
                remove = fruits[start]
                types[remove] -= 1
                if types[remove] == 0:
                    del types[remove]
                start += 1
            ans = max(ans, end - start + 1)
            end += 1

        return ans