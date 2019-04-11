class Solution:
    def letterCombinations(self, digits):
        pad = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        from collections import deque
        ans = deque()
        for n in digits:
            if ans:
                for i in range(len(ans)):
                    ss = ans.popleft()
                    for char in pad[n]:
                        ans.append(ss + char)
            else:
                ss = ''
                for char in pad[n]:
                    ans.append(ss+char)

        return list(ans)


print(Solution().letterCombinations('3'))
