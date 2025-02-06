from collections import defaultdict
from bisect import bisect_left


class Solution:
    def minimumDifference(self, nums):
        def subset_a(cur, start, count):
            if len(cur) <= count:
                group_a[len(cur)].append(cur[:])

            for i in range(start, mid):
                cur.append(nums[i])
                subset_a(cur, i + 1, count)
                cur.pop()

        def subset_b(cur, start, count):
            if len(cur) <= count:
                group_b[len(cur)].append(cur[:])

            for i in range(start, n):
                cur.append(nums[i])
                subset_b(cur, i + 1, count)
                cur.pop()

        n = len(nums)
        total_sum = sum(nums)
        answer = float('inf')
        mid = int(n / 2)
        group_a = defaultdict(list)
        group_b = defaultdict(list)

        subset_a([], 0, mid)
        subset_b([], mid, mid)

        for key, value in group_a.items():
            group_a[key] = [sum(v) for v in value]

        for key, value in group_b.items():
            group_b[key] = sorted([sum(v) for v in value])

        for i in range((mid + 1) // 2 + 1):
            a_count = i
            b_count = mid - i

            for a_sum in group_a[a_count]:
                target = total_sum / 2 - a_sum
                right = bisect_left(group_b[b_count], target)
                left = right - 1

                for candidate in [left, right]:
                    if 0 <= candidate < len(group_b[b_count]):
                        b_sum = group_b[b_count][candidate]
                        cur_sum = a_sum + b_sum
                        answer = min(answer, abs(cur_sum - (total_sum - cur_sum)))

        return answer


if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumDifference([2, -1, 0, 4, -2, -9]))  # 0
    print(solution.minimumDifference([34, 23, 30, 77, 85, 47, 96, 94]))  # 0
