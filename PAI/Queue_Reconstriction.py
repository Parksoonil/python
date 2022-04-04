import heapq
from pip import List


class Solution:
    def reconsturctQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))
        result = []
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])
        return result
s = Solution()
print(s.reconsturctQueue([[7,0], [4, 4], [7, 1], [5, 0], [6, 1],[7, 1]]))