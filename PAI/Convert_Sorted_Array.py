import collections
from pip import List

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    def printNode(self, n):
        if n is None:
            return 0
        queue = collections.deque([n])
        while queue:
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root != None:
                    print(cur_root.val, end = " ")
                    if cur_root.left:
                        queue.append(cur_root.left)
                    if cur_root.left and cur_root.right == None:
                        queue.append(None)
                    if cur_root.right:
                        queue.append(cur_root.right)
                    if cur_root.right and cur_root.left == None:
                        queue.append(None)
                if cur_root == None:
                    print(None, end = " ")
                    
class Solution:
    def sortedArray(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left = self.sortedArray(nums[:mid])
        node.right = self.sortedArray(nums[mid + 1:])
        return node
t = TreeNode()
s = Solution()
t.printNode(s.sortedArray([-10, -3, 0, 5, 9]))