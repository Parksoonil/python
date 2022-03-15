def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(1, total + 1):
        x = total / i
        if x >= i:
            if 2*x + 2*i == brown + 4:
                answer = [x, i]
    return answer
print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))