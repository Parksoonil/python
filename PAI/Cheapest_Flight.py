import collections
import heapq
from pip import List

class Solution:
    def findCheapestPrice(self, n: int, flight:List[List[int]], src: int,\
                            dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flight:
            graph[u].append((v, w))
        Q = [(0, src, K)]

        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k - 1))
        return -1
s = Solution()
print(s.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0))
print(s.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))