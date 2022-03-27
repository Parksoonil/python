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
    def isBalanced(self, root: TreeNode) -> bool:
        def check(root):
            if not root:
                return 0
            left = check(root.left)
            right = check(root.right)
            if left == -1 or \
                right == -1 or \
                    abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return check(root) != -1
s = Solution()
t = TreeNode()
n1 = TreeNode(3)
n2 = TreeNode(9)
n3 = TreeNode(20)
n4 = TreeNode(None)
n5 = TreeNode(None)
n6 = TreeNode(15)
n7 = TreeNode(7)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
print(s.isBalanced(n1))
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(2)
n4 = TreeNode(3)
n5 = TreeNode(3)
n6 = TreeNode(4)
n7 = TreeNode(4)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n4.left = n6
n4.right = n7
print(s.isBalanced(n1))