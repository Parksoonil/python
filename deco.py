def test(function):
    def wrapper():
        print("인사가 시작되었습니다.")
        function()
        print("인사가 종료되었습니다.")
@test
def hello():
    print("hello")
hello()