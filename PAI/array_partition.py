from pip import List

def array_pair(nums: List[int]) -> int:
    sum = 0
    pair = []
    nums.sort()
    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []
    return sum
print(array_pair([1, 4, 3, 2]))

def array_pair2(nums: List[int]) -> int:
    sum = 0
    nums.sort()
    for i, n in enumerate(nums):
        if i % 2 == 0:
            sum += n
    return sum
print(array_pair2([1, 4, 3, 2]))

def array_pair3(nums: List[int]) -> int:
    return sum(sorted(nums)[::2])
print(array_pair3([1, 4, 3, 2]))