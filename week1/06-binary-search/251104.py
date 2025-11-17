import math

class Solution:
    def search(self, nums, target):
        def binary(arr, left, right, target):
            if right < left:
                return -1
            
            center = left + math.ceil((right - left) / 2)

            if arr[center] == target:
                return center
            elif arr[center] < target:
                left = center + 1
            elif arr[center] > target:
                right = center - 1
            
            return binary(arr, left, right, target)

        left, right = 0, len(nums) - 1
        answer = binary(nums, left, right, target)
        return answer

class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1

if __name__ == '__main__':
    solution = Solution()
    print(solution.search([0, 1, 2, 3, 4, 5, 6], 4))
    print(solution.search([0, 1, 2, 3, 4, 5], 4))
    print(solution.search([0, 1, 2, 3, 4, 5, 6], 0))
    print(solution.search([0, 1, 2, 3, 4, 5], 0))
    print(solution.search([0, 1, 2, 3, 4, 5, 6], 6))
    print(solution.search([0, 1, 2, 3, 4, 5], 5))
    print(solution.search([0, 1, 2, 3, 4, 6, 7], 5))
    print(solution.search([0, 1, 2, 3, 4, 6], 5))
    print(solution.search([0, 1, 2, 3, 4, 5, 6], -1))
    print(solution.search([0, 1, 2, 3, 4, 5], -1))
    print(solution.search([0, 1, 2, 3, 4, 5, 6], 7))
    print(solution.search([0, 1, 2, 3, 4, 5], 7))
    