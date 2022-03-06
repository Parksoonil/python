user_input_a = input("정수 입력> ")

if user_input_a.isdigit():
    number_input_a = int(user_input_a)
    print("원의 반지름: ", number_input_a)
    print("원의 둘레: ", 2 * 3.14 * number_input_a)
    print("원의 넓이: ", 3.14 * number_input_a ** 2)
else:
    print("정수를 입력하지 않았습니다.")
print()
try: 
    number_input_b = int(input("정수 입력> "))
    print("원의 반지름: ", number_input_b)
    print("원의 둘레: ", 2 * 3.14 * number_input_b)
    print("원의 넓이: ", 3.14 * number_input_b ** 2)
except:
    print("무언가 잘못되었습니다.")
print()
list_input_a = ["52", "273", "32", "스파이", "103"]
list_number_a = []
for item in list_input_a:
    try:
        float(item)
        list_number_a.append(item)
    except:
        pass
print("{} 내부에 있는 숫자는".format(list_input_a))
print("{}입니다.".format(list_number_a))
print()
try:
    number_input_c = int(input("정수 입력> "))
except:
    print("정수를 입력하지 않았습니다.")
else:
    print("원의 반지름: ", number_input_c)
    print("원의 둘레: ", 2 * 3.14 * number_input_c)
    print("원의 넓이: ", 3.14 * number_input_c ** 2)