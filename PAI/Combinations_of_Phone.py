from pip import List

class Solution:
    def combinationsOfPhonoNum(self, digit: str) -> List[str]:
        result = []
        dic = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl",
                "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}
        def dfs(index, path):
            if len(path) ==len(digit):
                result.append(path)
                return
            for i in range(index, len(digit)):
                for j in dic[digit[i]]:
                    dfs(i + 1, path + j)
        if not digit:
            return []
        dfs(0, "")

        return result
s = Solution()
print(s.combinationsOfPhonoNum("23"))