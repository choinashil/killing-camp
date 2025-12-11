from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        window_count = defaultdict(int)
        formed = 0
        required = sum(t_count.values())
        answer = (float('inf'), 0, 0)

        l, r = 0, 0

        while r < len(s):
            char_r = s[r]

            if char_r in t_count:
                window_count[char_r] += 1
                if window_count[char_r] <= t_count[char_r]:
                    formed += 1

            while formed == required:
                if answer[0] > r - l + 1:
                    answer = (r - l + 1, l, r)

                char_l = s[l]
                if char_l in t_count:
                    window_count[char_l] -= 1
                    if window_count[char_l] < t_count[char_l]:
                        formed -= 1
                l += 1

            r += 1

        if answer[0] == float('inf'):
            return ''
        return s[answer[1]:answer[2] + 1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minWindow('ADOBECODEBANC', 'ABC'))  # 'BANC'
    print(solution.minWindow('a', 'a'))  # 'a'
    print(solution.minWindow('a', 'aa'))  # ''
    print(solution.minWindow('aab', 'aab'))  # 'aab'
