import bisect
from pip import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        child_i = cookie_j = 0
        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                child_i += 1
            cookie_j += 1
        return child_i

    def findContentChildren2(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        results = 0
        for i in s:
            index = bisect.bisect_right(g, i)
            if index > results:
                results += 1
        return results

s = Solution()
print(s.findContentChildren([1, 2, 3], [1, 1]))
print(s.findContentChildren([1, 2], [1, 2, 3]))
print(s.findContentChildren2([1, 2, 3], [1, 1]))
print(s.findContentChildren2([1, 2], [1, 2, 3]))