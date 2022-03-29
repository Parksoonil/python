import heapq
from pip import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = list()
        for n in nums:
            heapq.heappush(heap, -n)
        for _ in range(1, k):
            heapq.heappop(heap)
        return -heapq.heappop(heap)
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(len(nums) - k):
            heapq.heappop(nums)
        return heapq.heappop(nums)
    def findKthLargest3(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
    
s = Solution()
print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
print(s.findKthLargest2([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
print(s.findKthLargest3([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))