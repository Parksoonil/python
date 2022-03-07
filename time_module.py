import datetime
import time
from urllib import request
print("#현재 시간 출력하기")
now = datetime.datetime.now()
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
print()
print("#시간을 포맷에 맞춰 출력하기")
output_a = now.strftime("%Y.%m.%d %H:%M:%S")
output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,\
    now.month,\
    now.day,\
    now.hour,\
    now.minute,\
    now.second)
output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초")
print(output_a)
print(output_b)
print(output_c)
print()

print("# datetime.timedelta로 시간 더하기")
after = now + datetime.timedelta(\
    weeks = 1,\
    days = 1,\
    hours = 1,\
    minutes = 1,\
    seconds = 1)
print(after.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
print()
print("# now.replace()로 1년 더하기")
output = now.replace(year = (now.year + 1))
print(output.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
print()

target = request.urlopen("https://google.com")
output = target.read()
print(output)

print("지금부터 5초 동안 정지합니다!")
time.sleep(5)
print("프로그램을 종료합니다.")