def reverse(s: str) -> str:

    s.reverse()
    return s
print(reverse(["h", "e", "l", "l", "o"]))

def reverse2(s: str) -> str:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s
print(reverse2(["h", "e", "l", "l", "o"]))