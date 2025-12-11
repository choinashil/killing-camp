# top down


class Solution:
    def climbStairs(self, n):
        memo = {}

        def recursive(n):
            if n == 0 or n == 1:
                return 1

            if n not in memo:
                memo[n] = recursive(n - 1) + recursive(n - 2)

            return memo[n]

        return recursive(n)


# bottom up

class Solution:
    def climbStairs(self, n):
        memo = {
            0: 1,
            1: 1
        }

        for i in range(2, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]

        return memo[n]


# bottom up + 공간 최적화


class Solution:
    def climbStairs(self, n):
        prev, curr = 1, 1  # n=0, n=1일 때의 값

        for i in range(2, n + 1):
            prev, curr = curr, prev + curr

        return curr


if __name__ == '__main__':
    solution = Solution()
    print(solution.climbStairs(1))
    print(solution.climbStairs(2))
    print(solution.climbStairs(3))
    print(solution.climbStairs(4))
    print(solution.climbStairs(5))
