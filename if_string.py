number = int(input("정수 입력> "))

if number % 2 == 0:
    print("""\
        입력한 문자열은 {}입니다.
        {}는(은) 짝수입니다.""".format(number, number))
else:
    print("""\
    입력한 문자열은 {}입니다.
    {}는(은) 홀수입니다.""".format(number, number))

if number % 2 == 0:
    print("""입력한 문자열은 {}입니다. 
{}는(은) 짝수입니다.""".format(number, number))
else:
    print("""입력한 문자열은 {}입니다.
{}는(은) 홀수입니다.""".format(number, number))

if number % 2 == 0:
    print("""입력한 문자열은 {}입니다.\n{}는(은) 짝수입니다.""".format(number, number))
else:
    print("""입력한 문자열은 {}입니다.\n{}는(은) 홀수입니다.""".format(number, number))
print()

if number % 2 == 0:
    print((
        "입력한 문자열은 {}입니다.\n" 
        "{}는(은) 짝수입니다."
        ).format(number, number))
else:
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}는(은) 홀수입니다."
        ).format(number, number))
print()

if number % 2 == 0:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}는(은) 짝수입니다."
    ]).format(number, number))
else:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}는(은) 홀수입니다."
    ]).format(number, number))
print()

test = (
    "이렇게 입력해도 "
    "하나의 문자열로 연결되어 "
    "생성됩니다."
)
print('test: ', test)
print("type(test): ", type(test))
print()