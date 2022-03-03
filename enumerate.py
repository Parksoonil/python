example_list = ["A요소", "B요소", "C요소"]

print("#그냥 출력")
print(example_list)
print()

print("#enumerate() 함수 적용 출력")
print(enumerate(example_list))
print()
print("# list() 함수로 강제 변환 출력")
print(list(enumerate(example_list)))
print()

print("# 반복문과 조합하기")
for i, value in enumerate(example_list):
    print("{} 번쨰 요소는 {}입니다.".format(i, value))