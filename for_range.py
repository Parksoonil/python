for i in range(5):
    print(str(i) + " = 반복 변수")
print()
for i in range(5, 10):
    print(str(i) + " = 반복 변수")
print()
for i in range(0, 10, 3):
    print(str(i) + " = 반복 변수")
print()
array = [273, 32, 103, 57, 52]
for i in range(len(array)):
    print("{}번째 반복: {}".format(i, array[i]))
print()
for i in range(4, 0 - 1, -1):
    print("현재 반복 변수: {}".format(i))
print()
for i in reversed(range(5)):
    print("현재 반복 변수: {}".format(i))
print("\n\n\n")
i = 0
while i < 10:
    print("{}번째 반복입니다.".format(i))
    i += 1