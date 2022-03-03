array = []
for i in range(0, 20, 2):
    array.append(i * i)
print(array)

array1 = [i * i for i in range(0, 20, 2)]
print(array1)

array2 = ["사과","자두","초콜릿","바나나","체리"]
output = [fruit for fruit in array2 if fruit != "초콜릿"]
print(output)