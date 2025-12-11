# class Solution:
#     def maxSubArray(self, nums):
#         INF = float('inf')
#         answer = -INF
#         sub_sum = 0
#         i = 0

#         while i < len(nums):
#             sub_sum += nums[i]

#             answer = max(answer, sub_sum)
#             if sub_sum < 0:
#                 sub_sum = 0

#             i += 1

#         return answer


class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        answer = nums[0]
        prev = nums[0]

        for i in range(1, n):
            if prev <= 0:
                prev = nums[i]
            else:
                prev = prev + nums[i]

            answer = max(answer, prev)

        return answer


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubArray([3, -5, 2, 1]))  # 3
    print(solution.maxSubArray([-3, -1, -2]))  # - 1
    print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(solution.maxSubArray([1]))  # 1
    print(solution.maxSubArray([5, 4, -1, 7, 8]))  # 23
