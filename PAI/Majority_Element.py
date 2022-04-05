import collections
from pip import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) > len(nums) // 2:
                return num
    def majorityElement2(self, nums: List[int]) -> int:
        counts = collections.defaultdict(int)
        for num in nums:
            if counts[num] == 0:
                counts[num] = nums.count(num)
            if counts[num] > len(nums) // 2:
                return num
    def majorityElement3(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        half = len(nums) // 2
        a = self.majorityElement3(nums[:half])
        b = self.majorityElement3(nums[half:])

        return [b, a][nums.count(a) > half]
s = Solution()
print(s.majorityElement([3, 2, 3]))
print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))
print(s.majorityElement2([3, 2, 3]))
print(s.majorityElement2([2, 2, 1, 1, 1, 2, 2]))
print(s.majorityElement3([3, 2, 3]))
print(s.majorityElement3([2, 2, 1, 1, 1, 2, 2]))