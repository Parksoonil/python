def longest_palin(word: str) -> str:
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(word) and word[left] == word[right]:
            left -= 1
            right += 1
        return word[left + 1:right]

    if len(word) < 2 or word == word[::-1]:
        return word
    result = ''
    for i in range(len(word) - 1):
        result = max(result,
                        expand(i, i + 1),
                        expand(i, i + 2),
                        key = len)
    return result
print(longest_palin("babad"))