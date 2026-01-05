from collections import deque

# BFS


class Solution:
    def coinChange1(self, coins, amount):
        q = deque()
        visited = set()

        q.append((0, 0))
        visited.add(0)

        while q:
            cur_sum, cur_count = q.popleft()

            if cur_sum == amount:
                return cur_count

            for coin in coins:
                next_sum = cur_sum + coin

                if next_sum not in visited and next_sum <= amount:
                    q.append((next_sum, cur_count + 1))
                    visited.add(next_sum)

        return -1

# DP


class Solution:
    def coinChange(self, coins, amount):
        INF = float('inf')
        memo = [INF] * (amount + 1)
        memo[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    memo[i] = min(memo[i], memo[i - coin] + 1)

        return memo[amount] if memo[amount] != INF else -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.coinChange([1, 2, 5], 11))  # 3
    print(solution.coinChange([2], 3))  # -1
    print(solution.coinChange([1], 0))  # 0
    print(solution.coinChange([1, 3, 4], 6))  # 2
    print(solution.coinChange([1, 2, 5], 100))  # 20
