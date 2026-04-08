import math
from typing import Tuple


class Solution(object):
    def maxSubArray(self, nums) -> Tuple[int, int, int]:
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = float('-inf')
        current_max = 0
        start_index = -1
        end_index = -1

        for i in range(len(nums)):
            if current_max == 0:
                start_index = i
            current_max += nums[i]

            if maximum < current_max:
                maximum = current_max
                end_index = i

            if current_max < 0:
                current_max = 0
        return maximum, start_index, end_index

if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
