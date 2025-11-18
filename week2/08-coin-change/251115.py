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
                if coin <= amount:
                    next_amount = cur_amount + coin

                    if next_amount not in visited and next_amount <= amount:
                        q.append((next_amount, count + 1))
                        visited.add(next_amount)

        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.coinChange([1, 2, 5], 11))  # 3
    print(solution.coinChange([2], 3))  # -1
    print(solution.coinChange([1], 0))  # 0
    print(solution.coinChange([1, 3, 4], 6))  # 2
    print(solution.coinChange([1, 10], 3))  # 3
    print(solution.coinChange([2, 10], 3))  # -1
