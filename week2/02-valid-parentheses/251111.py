class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []

        for b in s:
            if b in bracket_dict:
                stack.append(b)
            else:
                if not stack:
                    return False

                if b == bracket_dict[stack[-1]]:
                    stack.pop()
                else:
                    return False

        return False if stack else True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid('()'))
    print(solution.isValid('()[]{}'))
    print(solution.isValid('(]'))
    print(solution.isValid('([])'))
    print(solution.isValid('([)]'))
