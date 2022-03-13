from collections import deque
def solution(prices):
    answer = []
    quene = deque(prices)
    while quene:
        p = quene.popleft()
        time = 0
    
        for q in quene:
            time += 1
            if p > q:
                break
        answer.append(time)
    return answer
print(solution([1, 2, 3, 2, 3]))

def solution2(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer
print(solution2([1, 2, 3, 2, 3]))