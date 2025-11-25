from heapq import heappop, heappush


class Solution:
    def smallestRange(self, nums):
        pq = []
        INF = float('inf')
        result = [-INF, INF]
        max_val = -INF

        for list_idx in range(len(nums)):
            val = nums[list_idx][0]
            max_val = max(max_val, val)
            heappush(pq, (val, list_idx, 0))

        print(pq)
        print(max_val)

        flag = True

        while flag:
            cur_val, cur_list_idx, cur_item_idx = heappop(pq)

            a, b = result[0], result[1]
            c, d = cur_val, max_val

            if not (a < c if b - a == d - c else b - a < d - c):
                result = [cur_val, max_val]

            if cur_item_idx == len(nums[cur_list_idx]) - 1:
                flag = False
            else:
                next_val = nums[cur_list_idx][cur_item_idx + 1]
                max_val = max(max_val, next_val)
                heappush(pq, (next_val, cur_list_idx, cur_item_idx + 1))

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))
    print(solution.smallestRange([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))
