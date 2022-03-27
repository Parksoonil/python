

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    def printNode(self, n):
        if n != None:
            print(n.val, end=" ")
        if n.left:
            self.printNode(n.left)
        if n.right:
            self.printNode(n.right)
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            node = TreeNode(t1.val + t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)

            return node
        else:
            return t1 or t2
t = TreeNode()
s = Solution()
t1 = TreeNode(1)
n1 = TreeNode(3)
n2 = TreeNode(2)
n3 = TreeNode(5)
t1.left = n1
t1.right = n2
n1.left = n3
t2 = TreeNode(2)
n4 = TreeNode(1)
n5 = TreeNode(3)
n6 = TreeNode(4)
n7 = TreeNode(7)
t2.left = n4
t2.right = n5
n4.right = n6
n5.right = n7
t.printNode(s.mergeTrees(t1, t2))