number = input("정수입력> ")
number = int(number)
if number > 0:
    print("양수입니다.")
if number < 0:
    print("음수입니다.")
if number == 0:
    print("0 입니다.")

print()
import datetime
now = datetime.datetime.now()
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
print("{} 년 {}월 {}일 {}시 {}분 {}초".format(
    now.year, now.month, now.day, now.hour, now.minute, now.second))
if now.hour < 12:
    print("현재시각은 {}시로 오전입니다.".format(now.hour))
if now.hour >= 12:
    print("현재시각은 {}시로 오후입니다.".format(now.hour))
if 3 <= now.month <=5:
    print("이번 달은 {}월로 봄입니다.".format(now.month))
if 6 <= now.month <=8:
    print("이번 달은 {}월로 여름입니다.".format(now.month))
if 9 <= now.month <=11:
    print("이번 달은 {}월로 가을입니다.".format(now.month))
if 1 <= now.month <=2 or now.month == 12:
    print("이번 달은 {}월로 겨울입니다.".format(now.month))