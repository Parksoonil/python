charcacter = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
    },
    "skill": ["베기","세게 베기","아주 세게 베기"]
}
for key in charcacter:
    if type(charcacter[key]) is dict:
        for small_key in charcacter[key]:
            print(small_key, " : ", charcacter[key][small_key])
    elif type(charcacter[key]) is list:
        for element in charcacter[key]:
            print(key, " : ", element)
    else:
        print(key, " : ", charcacter[key])