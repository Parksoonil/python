import test_module as test

radius = test.number_input()
print(test.get_circumference(radius))
print(test.get_circle_area(radius))

print("#메인의 __name__ 출력하기")
print(__name__)
print()