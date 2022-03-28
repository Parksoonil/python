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
                    if cur_root.left == None:
                        queue.append(None)
                    if cur_root.left:
                        queue.append(cur_root.left)
                    if cur_root.right == None:
                        queue.append(None)
                    if cur_root.right:
                        queue.append(cur_root.right)    
                if cur_root == None:
                    print(None, end = " ")
class Solution:
    val: int = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)
        return root  
t = TreeNode()
s = Solution()
n1 = TreeNode(4)
n2 = TreeNode(1)
n3 = TreeNode(6)
n4 = TreeNode(0)
n5 = TreeNode(2)
n6 = TreeNode(5)
n7 = TreeNode(7)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n4.left = None
n4.right = None
n5.left = None
n5.right = TreeNode(3)
n6.left = None
n6.right = None
n7.left = None
n7.right = TreeNode(8)
t.printNode(s.bstToGst(n1))    