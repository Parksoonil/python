def factorial(n):
    output = 1
    for i in range(1, n + 1):
        output *= i
    return output
print("1!: ", factorial(1))
print("2!: ", factorial(2))
print("3!: ", factorial(3))
print("4!: ", factorial(4))
print("5!: ", factorial(5))
print()
def factorial2(n):
    if n == 0:
        return 1
    else:
        return n * factorial2(n - 1)
print("1!: ", factorial2(1))
print("2!: ", factorial2(2))
print("3!: ", factorial2(3))
print("4!: ", factorial2(4))
print("5!: ", factorial2(5))