class Parent:
    def __init__(self):
        self.value = "테스트"
        print("parent 클래스의 __init()__ 메소드가 호출되었습니다.")
    def test(slef):
        print("Parent 클래스의 test() 메소드입니다.")
class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("Child 클래스의 _init()__ 메소드가 호출되었습니다.")
child = Child()
child.test()
print(child.value)
print()

class CustomException(Exception):
    def __init__(self):
        Exception.__init__(self)
        print("#### 내가 만든 오류가 생성되었어요! ####")
    def __str__(self):
        return "오류가 발생했어요"
raise CustomException
