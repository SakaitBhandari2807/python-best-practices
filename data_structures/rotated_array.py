class Solution:
    def rotate(self, nums, t):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left+ right)//2

            if nums[mid] == t:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= t < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < t <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

if __name__ == "__main__":
    solution = Solution()
    nums = [4,5,6,7,0,1,2]
    k = 0
    print(solution.rotate(nums, k))
