from heapq import heappop, heappush


class Solution:
    def smallestRange(self, nums):
        INF = float('inf')
        min_range = [-INF, INF]

        pq = []
        max_val = -INF

        for i in range(len(nums)):
            val = nums[i][0]
            max_val = max(max_val, val)
            heappush(pq, (val, i, 0))

        while pq:
            min_val, list_idx, item_idx = heappop(pq)

            a, b = min_range[0], min_range[1]
            c, d = min_val, max_val

            if not (a < c if b - a == d - c else b - a < d - c):
                min_range = [c, d]

            if item_idx == len(nums[list_idx]) - 1:
                break

            next_val = nums[list_idx][item_idx + 1]
            max_val = max(max_val, next_val)
            heappush(pq, (next_val, list_idx, item_idx + 1))

        return min_range


if __name__ == '__main__':
    solution = Solution()
    print(solution.smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))
    print(solution.smallestRange([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))
