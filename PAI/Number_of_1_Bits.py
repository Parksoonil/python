class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
    def hammingWeight2(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count
s = Solution()
print(s.hammingWeight(0b00000000000000000000000000001011))
print(s.hammingWeight(0b00000000000000000000000010000000))
print(s.hammingWeight(0b11111111111111111111111111111101))
print(s.hammingWeight2(0b00000000000000000000000000001011))
print(s.hammingWeight2(0b00000000000000000000000010000000))
print(s.hammingWeight2(0b11111111111111111111111111111101))