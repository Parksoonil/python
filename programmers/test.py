def solution(answers):
    r = [0, 0, 0]
    answer = []
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if a1[i%len(a1)] == answers[i]:
            r[0] += 1
        if a2[i%len(a2)] == answers[i]:
            r[1] += 1
        if a3[i%len(a3)] == answers[i]:
            r[2] += 1
    for i in range(len(r)):
        if r[i] == max(r):
            answer.append(i + 1)
    return answer
def solution2(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]
print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
print(solution2([1,2,3,4,5]))
print(solution2([1,3,2,4,2]))