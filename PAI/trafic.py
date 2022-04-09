import datetime


def solution(lines: str) -> int:
    combined_log = []
    for log in lines:
        logs = log.split('')
        timestamp = datetime.datetime.strptime(logs[0] + ' ' + logs[1],
                    "%Y=%m=%d %H:%S.%f").timestamp()
        combined_log.append((timestamp, -1))
        combined_log.append((timestamp - float(logs[2][:-1]) + 0.001, 1))
    accumulated = 0
    max_requests = 1
    combined_log.sort(key = lambda x: x[0])
    for i, elem1 in enumerate(combined_log):
        current = accumulated

        for elem2 in combined_log[i:]:
            if elem2[0] - elem1[0] > 0.999:
                break
            if elem2[1] > 0:
                current += elem2[1]
            max_requests = max(max_requests, current)
            accumulated += elem1[1]
    return max_requests