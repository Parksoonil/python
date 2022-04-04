import collections
from pip import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        result = 0
        counter = collections.Counter(tasks)

        while True:
            sub_count = 0
            for task, _ in counter.most_common(n + 1):
                sub_count += 1
                result += 1
                counter.subtract(task)
                counter += collections.Counter()
            if not counter:
                break
            result += n - sub_count + 1
        return result
s = Solution()
print(s.leastInterval(["A", "A",'A', 'B', 'B', 'B'], 2))