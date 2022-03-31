import heapq
from pip import List

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for(x, y) in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, (dist, x, y))
        result = []
        for _ in range(K):
            (dist, x, y) = heapq.heappop(heap)
            result.append((x, y))
        return result
s = Solution()
print(s.kClosest([[1, 3], [-2, 2]], 1))
print(s.kClosest([[3, 3], [5, -1], [-2, 4]],2))