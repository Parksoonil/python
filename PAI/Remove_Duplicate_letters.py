import collections

class solution(object):
    def removeDuplicateLatters(self, s: str) -> str:
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            if set(s) == set(suffix):
                return char + self.removeDuplicateLatters(suffix.replace(char, ""))
        return ""
    def removeDuplicateLatters2(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
        return ''.join(stack)

a = solution()
print(a.removeDuplicateLatters("dcabc"))
print(a.removeDuplicateLatters2("dcabc"))