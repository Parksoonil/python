def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i + 1]):
            if phone_book[i + 1][:len(phone_book[i])]\
            == phone_book[i]:
                answer = False
                break
    return answer
def solution2(phone_book):
    phone_book = sorted(phone_book)

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True
print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))

print(solution2(["119", "97674223", "1195524421"]))
print(solution2(["123", "456", "789"]))
print(solution2(["12", "123", "1235", "567", "88"]))