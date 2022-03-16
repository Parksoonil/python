def reorder(logs: str) -> str:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits
print(reorder(["dig2 3", "let1 art", "dig1 8", "let2 own", "let3 art"]))