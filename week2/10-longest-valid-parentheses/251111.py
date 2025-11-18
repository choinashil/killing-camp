class Solution:
    def longestValidParentheses(self, s):
        score = [0] * len(s)
        stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    index = stack.pop()
                    score[index] = 1
                    score[i] = 1

        answer, temp = 0, 0

        for s in score:
            if s:
                temp += s
            else:
                answer = max(answer, temp)
                temp = 0

        return max(answer, temp)


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestValidParentheses(''))
    print(solution.longestValidParentheses('()'))
    print(solution.longestValidParentheses('(()'))
    print(solution.longestValidParentheses(')()'))
    print(solution.longestValidParentheses(')(()()))'))
    print(solution.longestValidParentheses('(((())))'))
    print(solution.longestValidParentheses(')(()(()('))
    print(solution.longestValidParentheses(')(()((())('))
