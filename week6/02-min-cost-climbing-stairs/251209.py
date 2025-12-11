class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        memo = {}

        memo[0] = cost[0]
        memo[1] = cost[1]

        for i in range(2, n):
            if i not in memo:
                memo[i] = min(memo[i - 1], memo[i - 2]) + cost[i]

        return min(memo[n - 1], memo[n - 2])


if __name__ == '__main__':
    solution = Solution()
    print(solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
