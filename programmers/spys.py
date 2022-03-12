def solution(clothes):
    answer = 1
    cloth_type = {}
    for i in clothes:
        if i[1] in cloth_type:
            cloth_type[i[1]] += 1
        else:
            cloth_type[i[1]] = 2
    for i in cloth_type.values():
        answer *= i
    answer -= 1

    return answer
print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))

def solution2(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
print(solution2([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution2([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))
