import math
from itertools import permutations

def prime_num(n):
    if n == 0 or n == 1:
        return False
    else:
        for k in range(2, int(math.sqrt(n)) + 1):
            if n % k == 0:
                return False
        return True

def solution(numbers):
    answer = []
    arr = []
    num = 0
    for i in range(len(numbers)):
        arr = list(permutations(numbers, i + 1))
        for j in range(len(arr)):
            num = int(''.join(map(str, arr[j])))
            if prime_num(num):
                answer.append(num)
    answer = list(set(answer))
    return len(answer)
print(solution("17"))
print(solution("011"))

def solution2(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
print(solution2("17"))
print(solution2("011"))