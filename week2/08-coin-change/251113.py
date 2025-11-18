from collections import deque


class Solution:
    def coinChange(self, coins, amount):
        def bfs(start, count):
            q = deque()
            q.append([start, count])

            visited = set()

            while q:
                cur_amount, count = q.popleft()

                if cur_amount == amount:
                    return count
                elif all(v[0] > amount for v in q) and cur_amount > amount:
                    return -1

                for coin in coins:
                    next_amount = cur_amount + coin
                    if next_amount not in visited:
                        q.append([next_amount, count + 1])
                        visited.add(next_amount)

        return bfs(0, 0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.coinChange([1, 2, 5], 11))
    print(solution.coinChange([2], 3))
    print(solution.coinChange([1], 0))
    print(solution.coinChange([1, 3, 4], 6))
    print(solution.coinChange([1, 2147483647], 2))
    print(solution.coinChange([384, 324, 196, 481], 285))
    print(solution.coinChange([5], 7))
