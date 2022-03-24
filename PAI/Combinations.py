import itertools
from pip import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def dfs(elements, start: int, k: int):
            if k == 0:
                result.append(elements[:])
                return
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()
        dfs([], 1, k)
        return result
    def combine2(self, n: int, k:int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n + 1), k))
s = Solution()
print(s.combine(5, 3))
print(s.combine2(5, 3))