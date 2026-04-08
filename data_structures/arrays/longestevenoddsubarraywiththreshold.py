from typing import List


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        maximum_subarray = 0
        i = 0
        while i < len(nums):
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                l = i
                r = i + 1

                while r < len(nums):
                    if nums[r] % 2 !=  nums[r - 1] % 2 and nums[r] <= threshold:
                        r += 1
                    else:
                        break

                i = r
                maximum_subarray = max(maximum_subarray, r - l )
            else:
                i += 1
        return maximum_subarray

s = Solution()
print(s.longestAlternatingSubarray([3,2,5,4], 5))
print(s.longestAlternatingSubarray([1,2], 2))
print(s.longestAlternatingSubarray([2,3,4,5], 4))
print(s.longestAlternatingSubarray([4], 1))
print(s.longestAlternatingSubarray([4, 3, 1], 4))
