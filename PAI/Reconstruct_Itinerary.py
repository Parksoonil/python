import collections
from pip import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)
        route = []
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)
        dfs("JFK")
        return route[::-1]
    def findItinerary2(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets, reverse = True): #역순으로 정렬
            graph[a].append(b)
        route = []
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)
        dfs("JFK")
        return route[::-1]
    def findItinerary3(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)
        route, stack = [], ["JFK"]
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())
        return route[::-1]
s = Solution()
print(s.findItinerary([['MUC', 'LHR'], ['JFK', 'MUC'], ['SFO', 'SSJC'], ['LHR', 'SFO']]))
print(s.findItinerary([['JFK', 'SFO'], ['JFK', 'ATL'], ['SFO', 'ATL'], ['ATL', 'JFK'], ['ATL', 'SFO']]))
print(s.findItinerary2([['MUC', 'LHR'], ['JFK', 'MUC'], ['SFO', 'SSJC'], ['LHR', 'SFO']]))
print(s.findItinerary2([['JFK', 'SFO'], ['JFK', 'ATL'], ['SFO', 'ATL'], ['ATL', 'JFK'], ['ATL', 'SFO']]))
print(s.findItinerary3([['MUC', 'LHR'], ['JFK', 'MUC'], ['SFO', 'SSJC'], ['LHR', 'SFO']]))
print(s.findItinerary3([['JFK', 'SFO'], ['JFK', 'ATL'], ['SFO', 'ATL'], ['ATL', 'JFK'], ['ATL', 'SFO']]))
