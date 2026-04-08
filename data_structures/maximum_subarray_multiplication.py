class Solution():
    def maxSubArray(self, nums) ->  int:
        n = len(nums)
        prefix, suffix = 1, 1
        maximum = float('-inf')
        for i in range(n):
            prefix *= nums[i]
            suffix *= nums[n - i - 1]

            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1

            maximum = max(maximum, max(prefix, suffix))
        return maximum



s = Solution()
nums = [[1, 2, 3, 4, 5], [-1, 2, -3, 4], [1, 4, -3, 2], [1, 4, -3, 5], [-2, 3, 4, -1, 0, -2, 3, 1]]

for num in nums:
    print(s.maxSubArray(num))