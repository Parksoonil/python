[a, b] = [10, 20]
(c, d) = (10, 20)
print("a: ", a)
print("b: ", b)
print("c: ", c)
print("d: ", d)
print()
tuple_test = 10, 20, 30, 40
print("#괄호가 없는 튜플의 값과 자료형 출력")
print("tuple_test: ", tuple_test)
print("type(tuple)test): ", type(tuple_test))
print()
a, b, c = 10, 20, 30
print("#괄호가없는 튜플을 활용한 할당")
print("a: ", a)
print("b: ", b)
print("c: ", c)
print()
a, b = 10, 20
print("#교환 전 값")
print("a: ", a)
print("b: ", b)
print()
a, b = b, a
print("#교환 후 값")
print("a: ", a)
print("b: ", b)
print()

def test():
    return (10, 20)
a, b = test()
print("a: ", a)
print("b: ", b)
