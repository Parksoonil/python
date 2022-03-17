from pip import List

def two_sum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in (i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
print(two_sum([2, 7, 11, 15], 9))

def two_sum2(nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        complement = target - n
        if complement in nums[i + 1:]:
            return [ nums.index(n), nums[i + 1:].index(complement) + (i + 1)]
print(two_sum2([2, 7, 11, 15], 9))

def two_sum3(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return[i, nums_map[target - num]]
print(two_sum3([2, 7, 11, 15], 9))

def two_sum4(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return[nums_map[target - num], i]
        nums_map[num] = i
print(two_sum4([2, 7, 11, 15], 9))