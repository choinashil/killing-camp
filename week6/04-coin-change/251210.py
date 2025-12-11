# bottom up
class Solution:
    def coinChange(self, coins, amount):
        INF = float('inf')
        memo = [INF] * (amount + 1)
        memo[0] = 0

        def dp(n):
            for coin in coins:
                if n - coin >= 0:
                    memo[n] = min(memo[n], memo[n - coin] + 1)

        for n in range(1, amount + 1):
            dp(n)

        return -1 if memo[amount] == INF else memo[amount]


# top down
class Solution:
    def coinChange(self, coins, amount):
        INF = float('inf')
        memo = [INF] * (amount + 1)
        memo[0] = 0

        def recursive(n):
            if memo[n] != INF:
                return memo[n]

            for coin in coins:
                if n - coin >= 0:
                    memo[n] = min(memo[n], recursive(n - coin) + 1)

            return memo[n]

        recursive(amount)
        return -1 if memo[amount] == INF else memo[amount]


if __name__ == '__main__':
    solution = Solution()
    print(solution.coinChange([1, 3, 4], 6))  # 2
    print(solution.coinChange([1, 2, 5], 11))  # 3
    print(solution.coinChange([2], 3))  # -1
    print(solution.coinChange([1], 0))  # 0
