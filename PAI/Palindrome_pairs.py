import collections
from pip import List
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = []
class Trie:
    def __init__(self):
        self.root = TrieNode()
    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word[::] == word[::-1]
    def insert(self, index, word) -> None:
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[0: len(word) - i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
        node.word_id = index
    def search(self, index, word) -> List[List[int]]:
        result = []
        node = self.root
        while word:
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])
        return result


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(word):
            return word == word[::-1]
        output = []
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i == j:
                    continue
                if is_palindrome(word1 + word2):
                    output.append([i, j])
        return output
    def palindromePairs2(self, words: List[str]) -> List[List[int]]:
        trie = Trie()
        for i, word in enumerate(words):
            trie.insert(i, word)
        result = []
        for i, word in enumerate(words):
            result.extend(trie.search(i, word))
        return result
s = Solution()
print(s.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))
print(s.palindromePairs(["bat", "tab", "cat"]))
print(s.palindromePairs2(["abcd", "dcba", "lls", "s", "sssll"]))
print(s.palindromePairs2(["bat", "tab", "cat"]))