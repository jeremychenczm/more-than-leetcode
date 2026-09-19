class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def bt(i, path):
            if i == len(digits):
                ans.append(''.join(path))
                return
            
            for c in letters[digits[i]]:
                path.append(c)
                bt(i + 1, path)
                path.pop()

        ans = []
        bt(0, [])
        return ans
        