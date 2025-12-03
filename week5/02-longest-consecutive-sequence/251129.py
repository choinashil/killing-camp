class Solution:
    def longestConsecutive(self, nums):
        answer = 0
        num_dict = {num: True for num in nums}

        for num in num_dict:
            if num - 1 not in num_dict:
                count = 1
                next_num = num + 1

                while next_num in num_dict:
                    count += 1
                    next_num += 1

                answer = max(answer, count)

        return answer


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))  # 4
    print(solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
    print(solution.longestConsecutive([1, 0, 1, 2]))  # 3
    print(solution.longestConsecutive([]))  # 0
    print(solution.longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))  # 7
