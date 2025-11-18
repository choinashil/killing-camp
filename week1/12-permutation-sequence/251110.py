class Solution(object):
    def getPermutation(self, n, k):
        count = 0
        s = set()
        result = None

        def backtrack(curr):
            nonlocal count, result

            if len(curr) == n:
                count += 1

                if count == k:
                    result = ''.join(curr)
                    return True

                return False

            for num in range(1, n + 1):
                if num not in s:
                    curr.append(str(num))
                    s.add(num)

                    if backtrack(curr):
                        return True

                    curr.pop()
                    s.remove(num)

            return False

        backtrack([])
        return result


if __name__ == '__main__':
    solution = Solution()

    print(solution.getPermutation(3, 1))
    print(solution.getPermutation(3, 3))
    print(solution.getPermutation(3, 6))
    print(solution.getPermutation(9, 278893))
