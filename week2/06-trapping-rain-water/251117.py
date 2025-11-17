class Solution:
    def trap(self, height):
        water = 0
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]

        while l < r:
            if max_l <= max_r:
                if height[l] < max_l:
                    water += max_l - height[l]
                else:
                    max_l = height[l]
                l += 1
            else:
                if height[r] < max_r:
                    water += max_r - height[r]
                else:
                    max_r = height[r]
                r -= 1

        return water

if __name__ == '__main__':
    solution = Solution()
    print(solution.trap([2,0,2])) # 2
    print(solution.trap([1,0,2])) # 1 
    print(solution.trap([1,0,0,2])) # 2
    print(solution.trap([1,0,0,2,3])) # 2 
    print(solution.trap([2,0,1,2,3])) # 3
    print(solution.trap([0,2,0,1,0,0,3])) # 7 
    print(solution.trap([0,1,2,0,0,1,3])) # 5
    print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
    print(solution.trap([4,2,0,3,2,5])) # 9
