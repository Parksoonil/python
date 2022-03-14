def solution(operations):
    answer = []
    for data in operations:
        alpha, num = data.split()
        if alpha == 'I':
            answer.append(int(num))
        else:
            if len(answer) > 0:
                if num == '1':
                    answer.pop()
                else:
                    answer.pop(0)
            else:
                pass
        answer.sort()
    if len(answer) == 0:
        return [0, 0]
    return[max(answer), min(answer)]
print(solution(["I 16","D 1"]))
print(solution(["I 7","I 5","I -5","D -1"]))
import heapq
def solution2(operations):
    max_heap = []
    min_heap = []
    for i in operations:
        a, b = i.split()
        b = int(b)
        if a == 'I':
            heapq.heappush(max_heap, -b)
            heapq.heappush(min_heap, b)
        else:
            if b == 1:
                if max_heap != []:
                    heapq.heappop(max_heap)
                    if max_heap == [] or -max_heap[0] < min_heap[0]:
                        min_heap = []
                        max_heap = []
            elif b == -1:
                if min_heap != []:
                    heapq.heappop(min_heap)
                    if min_heap == [] or -max_heap[0] < min_heap[0]:
                        max_heap = []
                        min_heap = []
    if min_heap == []:
        return [0, 0]
    return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
print(solution2(["I 16","D 1"]))
print(solution2(["I 7","I 5","I -5","D -1"]))