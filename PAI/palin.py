def palin(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    while len(strs) > 1:
        if strs.pop() != strs.pop(0):
            return False
    return True        
print(palin("A man, a plan, a canal: Panama"))
print(palin("race a car"))

import collections
import re
from typing import Deque
def palin2(s: str) -> bool:
    strs:Deque = collections.deque()
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True
print(palin2("A man, a plan, a canal: Panama"))
print(palin2("race a car"))

def palin3(s: str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]','', s)
    return s == s[::-1]
print(palin3("A man, a plan, a canal: Panama"))
print(palin3("race a car"))
             