class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        start = 0
        c_dict = {}

        for i, c in enumerate(s):
            if c in c_dict and c_dict[c] >= start:
                answer = max(answer, i - start)
                start = c_dict[c] + 1

            c_dict[c] = i

        return max(answer, len(s) - start)


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring('abcabcbb'))  # 3
    print(solution.lengthOfLongestSubstring('bbbbb'))  # 1
    print(solution.lengthOfLongestSubstring('pwwkew'))  # 3
    print(solution.lengthOfLongestSubstring(' '))  # 1
    print(solution.lengthOfLongestSubstring('dvdf'))  # 3
    print(solution.lengthOfLongestSubstring('abba'))  # 2
    print(solution.lengthOfLongestSubstring('tmmzuxt'))  # 5
