class Solution(object):
    def partition(self, s):
        def backtrack(curr, start):
            if start == len(s):
                answer.append(curr[:])
                return

            for i in range(start, len(s)):
                substring = s[start:i + 1]
                if substring == substring[::-1]:
                    curr.append(substring)
                    backtrack(curr, i + 1)
                    curr.pop()

        answer = []
        backtrack([], 0)
        return answer


if __name__ == '__main__':
    solution = Solution()
    print(solution.partition(''))  # []
    print(solution.partition('a'))  # ['a']
    print(solution.partition('ab'))  # ['a', 'b]
    print(solution.partition('aab'))  # ['a', 'a', 'b'], ['aa', 'b']
    print(solution.partition('aabaa'))  # ['a', 'a', 'b', 'a', 'a'], ['aa', 'b', 'a', 'a'], ['aa', 'b', 'aa'], ['a', 'a', 'b', 'aa']
    print(solution.partition('aabc'))  # ['a', 'a', 'b', 'c'], ['aa','b','c']
    print(solution.partition('abcaca'))
    print(solution.partition('abcacac'))
