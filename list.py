list_a = [1, 2, 3]
list_b = [4, 5, 6]
print("#리스트")
print("list_a = ", list_a)
print("list_b = ", list_b)
print()
print("#리스트 기본 연산자")
print("list_a + list_b = ", list_a + list_b)
print("list_a * 3 = ", list_a * 3)
print()
print("#길이 구하기")
print("len(list_a) = ", len(list_a))
print()
print("#리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a)
print()
print("#리스트 중간에 요소 추가하기")
list_a.insert(0, 10)
print(list_a)
print()
list_a = [0, 1, 2, 3, 4, 5]
print("#리스트의 요소 하나 제거하기")
del list_a[1]
print("del list_a[1]: ", list_a)
list_a.pop(2)
print("pop(2): ", list_a)
print()
array = [273, 32, 103, 57, 52]
for element in array:
    print(element)