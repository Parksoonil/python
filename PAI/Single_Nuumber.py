from pip import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
s = Solution()
print(s.singleNumber([2, 2, 1]))
print(s.singleNumber([4, 2, 1, 2, 1]))