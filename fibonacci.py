from typing import Counter


def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n -1) + fibonacci(n - 2)
print("fibonacci(1): ", fibonacci(1))
print("fibonacci(2): ", fibonacci(2))
print("fibonacci(3): ", fibonacci(3))
print("fibonacci(4): ", fibonacci(4))
print("fibonacci(5): ", fibonacci(5))
print()
counter = 0

def fibonacci2(n):
    print("fibonacci({})를 구합니다.".format(n))
    global counter
    counter += 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci2(n - 1) + fibonacci2(n - 2)
fibonacci2(10)
print("---")
print("fibonacci(10)계산에 환용된 덧셈 횟수는 {}번 입니다.".format(counter))
print()
dictionary = {
    1: 1,
    2: 1
}
def fibonacci3(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci3(n - 1) + fibonacci3(n - 2)
        dictionary[n] = output
        return output
print("fibonacci(10): ", fibonacci3(10))
print("fibonacci(20): ", fibonacci3(20))
print("fibonacci(30): ", fibonacci3(30))
print("fibonacci(40): ", fibonacci3(40))
print("fibonacci(50): ", fibonacci3(50))
