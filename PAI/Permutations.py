import itertools
from pip import List

class Solution:
    def permutations(self, num: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []
        def dfs(elements):
            if len(elements) == 0:
                results.append(prev_elements[:])
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()
        dfs(num)
        return results
    def permutations2(self, num: List[int]) -> List[List[int]]:
        return list(itertools.permutations(num))
s = Solution()
print(s.permutations([1, 2, 3]))
print(s.permutations2([1, 2, 3]))