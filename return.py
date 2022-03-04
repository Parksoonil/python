def return_test():
    print("A위치")
    return
    print("B위치")
return_test()
print()
def return_test2():
    return 100
value = return_test2()
print(value)
print()
def return_test3():
    return
value = return_test3()
print(value)
print()
def sum_all(start, end):
    output = 0
    for i in range(start, end + 1):
        output += i
    return output
print("0 to 100: ", sum_all(0, 100))
print("0 to 1000: ", sum_all(0, 1000))
print("50 to 100: ", sum_all(50, 100))
print("500 to 1000: ", sum_all(500, 1000))
print()
def sum_all2(start = 0, end = 100, step = 1):
    output = 0
    for i in range(start, end + 1, step):
        output += i
    return output
print("A. ", sum_all2(0, 100,10))
print("B. ", sum_all2(end = 100))
print("C. ", sum_all2(end = 100, step = 2))