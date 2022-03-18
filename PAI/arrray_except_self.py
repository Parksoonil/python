from pip import List

def array_mul(nums: List[int]) -> List[int]:
    value = []
    v = 1
    for i in range(0, len(nums)):
        value.append(v)
        v *= nums[i]
    v = 1
    for i in range(len(nums) - 1, 0 - 1, -1):
        value[i] *= v
        v *= nums[i]
    return value
print(array_mul([1, 2, 3, 4]))

    
