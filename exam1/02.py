# 일자: 2025-11-23
# 시작: 16:56
# 종료: 17:06

from collections import deque


class Solution:
    def coinChange(self, coins, amount):
        q = deque()
        visited = set()

        q.append((0, 0))
        visited.add(0)

        while q:
            cur_amount, count = q.popleft()

            if cur_amount == amount:
                return count

            for coin in coins:
                next_amount = cur_amount + coin

                if coin <= amount and next_amount <= amount and next_amount not in visited:
                    q.append((next_amount, count + 1))
                    visited.add(next_amount)

        return -1


if __name__ == '__main__':
    solution = Solution()
    # print(solution.coinChange([1, 2, 5], 11))
    # print(solution.coinChange([2], 3))
    # print(solution.coinChange([1], 0))
    print(solution.coinChange([1, 2, 5], 100))
