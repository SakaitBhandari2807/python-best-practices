from typing import List


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:

        i = 1
        maximum_subarray = 0
        while i < len(nums):
            alternating_element = 1
            counter = 0
            j = i
            while j < len(nums) and nums[j] == nums[j - 1] + alternating_element:
                j += 1
                counter += 1
                if alternating_element == 1:
                    alternating_element = -1
                else:
                    alternating_element = 1
            i += 1
            if counter != 0:
                counter += 1
            maximum_subarray = max(maximum_subarray, counter)
        return maximum_subarray if maximum_subarray > 0 else -1


s = Solution()
print(s.alternatingSubarray([21,9,5]))
print(s.alternatingSubarray([2,3,4,3,4]))
print(s.alternatingSubarray([4,5,6]))