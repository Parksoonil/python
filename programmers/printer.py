def solution(priorities, location):
    answer = 0
    max_num = max(priorities)
    while True:
        for i in range(len(priorities)):
            if max_num == priorities[i]:
                answer += 1
                priorities[i] = 0
                max_num = max(priorities)
                if i == location:
                    return answer
print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))

def solution2(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
print(solution2([2, 1, 3, 2], 2))
print(solution2([1, 1, 9, 1, 1, 1], 0))