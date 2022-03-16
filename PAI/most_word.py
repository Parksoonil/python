import collections
import re

def most_word(words: str, banned: str):
    word = [char for char in re.sub(r'[^\w]', ' ', words)
                .lower().split()
                    if char not in banned]
    answer = collections.Counter(word).most_common(1)[0][0]
    return answer
print(most_word("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))