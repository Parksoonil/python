import collections
from pip import List


def solution(cacheSize: int, cities: List[str]) -> int:
    results = 0
    cache = collections.deque(maxlen= cacheSize)
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            results += 1
        if city not in cache:
            cache.append(city)
            results += 5
    return results
print(solution(3, ["je", "pang", "seo", "new", "la", "je", "pang", "seo", "new", "la"]))
print(solution(2, ["Je", "Pang", "New", "new"]))