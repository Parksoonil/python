import collections
from pip import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]])\
                -> bool:
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)
        traced = set()
        def dfs(i):
            if i in traced:
                return False
            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)
            return True
        for x in list(graph):
            if not dfs(x):
                return False
        return True
    def canFinish2(self, numCourses: int, prerequisites: List[List[int]])\
                -> bool:
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)
        traced = set()
        visited = set()

        def dfs(i):
            if i in traced:
                return False
            if i in visited:
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)
            visited.add(i)
            return True
        for x in list(graph):
            if not dfs(x):
                return False
        return True
s = Solution()
print(s.canFinish(2, [[1, 0]]))
print(s.canFinish(2, [[1, 0], [0, 1]]))
print(s.canFinish2(2, [[1, 0]]))
print(s.canFinish2(2, [[1, 0], [0, 1]]))