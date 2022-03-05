min = 2
max = 10
total = 100
meme = {}
def problem(n, r):
    key = str([n, r])
    if str in meme:
        return meme[key]
    if n < 0:
        return 0 #남은 사람이 0밑이면 무효
    if n == 0:
        return 1 #남은 사람이 0이면 카운트를 위해 1리턴
    count = 0
    for i in range(r, max + 1):
        count += problem(n - i, i)#(98,2), (96,2)...
    meme[key] = count
    return count
print(problem(100, 2))