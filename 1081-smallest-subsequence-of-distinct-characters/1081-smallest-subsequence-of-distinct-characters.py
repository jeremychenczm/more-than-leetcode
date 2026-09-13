class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occur = {c : i for i, c in enumerate(s)}
        stack = []
        in_stack = set()

        for i, c in enumerate(s):
            if c in in_stack:
                continue
            while stack and stack[-1] > c and last_occur[stack[-1]] > i:
                pop_ele = stack.pop()
                in_stack.remove(pop_ele)
                
            stack.append(c)
            in_stack.add(c)

        return ''.join(stack)