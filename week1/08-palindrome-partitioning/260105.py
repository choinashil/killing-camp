# 풀이 1
class Solution:
    def partition(self, s):
        def backtrack(cur, start):
            subsets.append(cur[:])

            for i in range(start, len(s)):
                cur.append(i)
                backtrack(cur, i + 1)
                cur.pop()

        def separate_string(subsets):
            strings = []
            for subset in subsets:
                str = []
                for i in range(0, len(subset)):
                    if i == len(subset) - 1:
                        str.append(s[subset[i]:])
                    else:
                        str.append(s[subset[i]:subset[i + 1]])

                strings.append(str)

            return strings

        def validate_strings(strings):
            valid_strings = []

            for string in strings:
                valid = True
                for char in string:
                    if char != char[::-1]:
                        valid = False
                        break

                if valid:
                    valid_strings.append(string)
            return valid_strings

        subsets = []
        backtrack([0], 1)
        strings = separate_string(subsets)
        answer = validate_strings(strings)

        return answer


# 풀이 2
class Solution:
    def partition(self, s):
        def backtrack(cur, start):
            if start == len(s):
                answer.append(cur[:])
                return

            for end in range(start, len(s)):
                substr = s[start:end + 1]

                if substr == substr[::-1]:
                    cur.append(substr)
                    backtrack(cur, end + 1)
                    cur.pop()

        answer = []
        backtrack([], 0)
        return answer


if __name__ == '__main__':
    solution = Solution()
    print(solution.partition("a"))  # [['a']]
    print(solution.partition("aab"))  # [['a', 'a', 'b'], ['aa', 'b']]
    print(solution.partition("aabb"))  # [['a', 'a', 'bb'], ['a', 'a', 'b', 'b'], ['aa', 'bb'], ['aa', 'b', 'b']]
    print(solution.partition("aabc"))  # [['a', 'a', 'b', 'c'], ['aa', 'b', 'c']]
    print(solution.partition("abcba"))  # [['abcba'], ['a', 'b', 'c', 'b', 'a'], ['a', 'bcb', 'a']]
