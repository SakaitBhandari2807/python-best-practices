import heapq

class Solution:
    def solve(self, nums, k):

        min_heap = nums[:k]
        heapq.heapify(min_heap)

        for elem in range(k, len(nums)):

            if nums[elem] > min_heap[0]:
                heapq.heapreplace(min_heap, nums[elem])

        return min_heap[0]

    def solve_kth_smallest(self, nums, k):
        max_heap = nums[:k]
        heapq.heapify(max_heap)
        for i in range(k, len(nums)):
            if nums[i] < max_heap[0]:
                heapq.heappush(max_heap, nums[i])

        return max_heap[0]

if __name__ == "__main__":
    nums = [3,2,3,1,2, 4,5,5,6]
    k = 4
    s = Solution()
    print(s.solve(nums, k))
    print(s.solve_kth_smallest(nums, k))