from pip import List


class Solution:
    def canCompleteCircit(self, gas: List[int], cost: List[int]) -> int:
        for start in range(len(gas)):
            fuel = 0
            for i in range(start, len(gas) + start):
                index = i % len(gas)
                can_travel = True
                if gas[index] + fuel < cost[index]:
                    can_travel = False
                    break
                else:
                    fuel += gas[index] - cost[index]
            if can_travel:
                return start
        return -1
    def canCompleteCircit2(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start, fuel = 0, 0
        for i in range(len(gas)):
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        return start
s = Solution()
print(s.canCompleteCircit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
print(s.canCompleteCircit2([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))