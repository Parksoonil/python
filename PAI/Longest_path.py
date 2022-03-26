class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    result: int = 0
    def longestPath(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0
            self.result = max(self.result, left + right)
            return max(left, right)
        dfs(root)
        return self.result
s = Solution()
n1 = TreeNode(5)
n2 = TreeNode(4)
n3 = TreeNode(5)
n4 = TreeNode(1)
n5 = TreeNode(1)
n6 = TreeNode(5)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.right = n6
print(s.longestPath(n1))

n1 = TreeNode(1)
n2 = TreeNode(4)
n3 = TreeNode(5)
n4 = TreeNode(4)
n5 = TreeNode(4)
n6 = TreeNode(5)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.right = n6
print(s.longestPath(n1))

