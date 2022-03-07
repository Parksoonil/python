import random as r
print("#random 모듈")

print("- random(): ", r.random())
print("- uniform(10, 20): ", r.uniform(10, 20))
print("- randrange(10): ", r.randrange(10))
print("- choice([1, 2, 3, 4, 5]): ", r.choice([1, 2, 3, 4, 5]))
print("- shuffle([1, 2, 3, 4, 5]): ", r.shuffle([1, 2, 3, 4, 5]))
print("- sample([1, 2, 3, 4, 5], k = 2): ", r.sample([1, 2, 3, 4, 5], k = 2))
print()

import os
print("현재 운영체제: ", os.name)
print("현재 폴더: ", os.getcwd())
print("현재 폴더 내부의 요소: ", os.listdir())

os.mkdir("hello")
os.rmdir("hello")

with open("original.txt", "w") as file:
    file.write("hello")
os.rename("original.txt", "new.txt")
os.remove("new.txt")
os.system("dir")
print()

import sys
print(sys.argv)
print("---")
print("getwindowsversion:()", sys.getwindowsversion())
print("---")
print("copyright: ", sys.copyright)
print("---")
print("version: ", sys.version)
sys.exit()