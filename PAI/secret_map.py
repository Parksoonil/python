from pip import List

def solution(n: int, arr1: List[int], arr2: List[int]) -> List[str]:
    map = []
    for i in range(n):
        map.append(bin(arr1[i] | arr2[i])[2:]
        .zfill(n)
        .replace("1", "#")
        .replace("0", " "))
    return map
print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))