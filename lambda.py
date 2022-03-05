power = lambda item: item * item
under_3 = lambda item: item < 3

list_input_a = [1, 2, 3, 4, 5]

output_a = map(power,list_input_a)
print("#map() 함수와 실행결과")
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a: ",list(output_a))
output_b = filter(under_3, list_input_a)
print("#filter() 함수의 실행결과")
print("filter(under_3, list_input_a): ", output_b)
print("filter(under_3, list_input_a): ", list(output_b))
print()

output_a = map(lambda item: item * item,list_input_a)
print("#map() 함수와 실행결과")
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a: ",list(output_a))
output_b = filter(lambda item: item < 3, list_input_a)
print("#filter() 함수의 실행결과")
print("filter(under_3, list_input_a): ", output_b)
print("filter(under_3, list_input_a): ", list(output_b))