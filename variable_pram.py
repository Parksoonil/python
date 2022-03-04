def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()
print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")
print()
def print_n_times2(value, n = 2):
    for i in range(n):
        print(value)
print_n_times2("안녕하세요")
print()
def print_n_times3(*values, n = 2):
    for i in range(n):
        for value in values:
            print(value)
        print()
print_n_times3("안녕하세요", "즐거운", "파이썬 프로그래밍", n = 3)
print()
def test(a, b = 10, c = 100):
    print(a + b + c)
test(10, 20, 30)
test(a = 10, b = 100, c = 200)
test(c = 10, a = 100, b = 200)
test(10, c = 200)