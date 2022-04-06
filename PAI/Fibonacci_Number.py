import collections


class Solution:
    dp = collections.defaultdict(int)
    dp2 = collections.defaultdict(int)
    def fib(self, N: int) -> int: #브루트 포스
        if N <= 1:
            return N
        return self.fib(N - 1) + self.fib(N - 2)
    def fib2(self, N: int) -> int: #메모이제이션
        if N <= 1:
            return N
        if self.dp[N]:
            return self.dp[N]
        self.dp[N] = self.fib(N - 1) + self.fib(N - 2)
        return self.dp[N]
    def fib3(self, N: int) -> int: #타뷸레이션
        self.dp2[0] = 0
        self.dp2[1] = 1

        for i in range(2, N + 1):
            self.dp2[i] = self.dp2[i - 1] + self.dp2[i - 2]
        return self.dp2[N]
    def fib4(self, N: int) -> int:
        x, y = 0, 1
        for i in range(0, N):
            x, y = y, x + y
        return x

s = Solution()
print(s.fib(5))
print(s.fib2(5))
print(s.fib3(5))
print(s.fib4(5))