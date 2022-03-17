import collections
from pip import List
def anagrams(words: List[str]) -> List[List[str]]:
    anagram = collections.defaultdict(list)
    for word in words:
        anagram["".join(sorted(word))].append(word)
    return list(anagram.values())
print(anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))