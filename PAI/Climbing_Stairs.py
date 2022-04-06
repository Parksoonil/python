import collections


class Solution:
    dp = collections.defaultdict(int)
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
    def climbStairs2(self, n: int) -> int:
        if n <= 2:
            return n
        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.climbStairs2(n - 1) + self.climbStairs2(n - 2)
        return self.dp[n]
s = Solution()
print(s.climbStairs(3))
print(s.climbStairs2(3))