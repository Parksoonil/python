class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')
s = Solution()
print(s.hammingDistance(1, 4))