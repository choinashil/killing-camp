class Solution:
    def trap(self, height):
        stack = []
        water = 0

        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                idx = stack.pop()

                if stack:
                    l = stack[-1]
                    r = i

                    h = min(height[l], height[r]) - height[idx]
                    w = r - l - 1
                    water += h * w

            stack.append(i)

        return water


if __name__ == "__main__":
    solution = Solution()
    print(solution.trap([2, 1, 0, 2]))  # 3
    print(solution.trap([0, 1, 0, 2, 3]))  # 1
    print(solution.trap([1, 2, 0, 0, 1, 2]))  # 5
    print(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
    print(solution.trap([4, 2, 0, 3, 2, 5]))  # 9
