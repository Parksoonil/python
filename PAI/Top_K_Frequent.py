import collections
import heapq
from pip import List

class Solution:
    def frequenet(self, nums: List, k: int) -> List:
        freq = collections.Counter(nums)
        result = []
        for i, n in enumerate(freq):
            if n >= 2:
                result.append(i)
        return result  

    def frequenet(self, nums: List, k: int) -> List:
        freq = collections.Counter(nums)
        result_heap = []
        for f in freq:
            heapq.heappush(result_heap, (-freq[f], f))
        topk = list()
        for _ in range(k):
            topk.append(heapq.heappop(result_heap)[1])
        return topk
    def frequenet(self, nums: List, k: int) -> List:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]
s = Solution()
print(s.frequenet([1, 1, 1, 2, 2, 3], 2))