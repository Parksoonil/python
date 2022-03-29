import sys
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    prev = -sys.maxsize
    result = sys.maxsize
    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)
        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val
        if root.right:
            self.minDiffInBST(root.right)
        return self.result

    def minDiffInBST2(self, root: TreeNode) -> int:
        prev = -sys.maxsize
        result = sys.maxsize
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result = min(result, node.val - prev)
            prev = node.val
            node = node.right

        return result
s = Solution()
n1 = TreeNode(4)
n2 = TreeNode(2)
n3 = TreeNode(6)
n1.left = n2
n1.right = n3
n2.left = TreeNode(1)
n2.right = TreeNode(3)
print(s.minDiffInBST(n1))
print(s.minDiffInBST2(n1))