import collections

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
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        return (root.val if L <= root.val <= R else 0) + \
                self.rangeSumBST(root.left, L, R) + \
                self.rangeSumBST(root.right, L, R)
    def rangeSumBST2(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(node: TreeNode):
            if not node:
                return 0
            if node.val < L:
                return dfs(node.right)
            elif node.val > R:
                return dfs(node.left)
            return node.val + dfs(node.left) + dfs(node.right)
        return dfs(root)
    def rangeSumBST3(self, root: TreeNode, L: int, R: int) -> int:
        stack, sum = [root], 0
        while stack:
            node = stack.pop()
            if node:
                if node.val > L:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
                if L <= node.val <= R:
                    sum += node.val
        return sum

s = Solution()
n1 =TreeNode(10)
n2 =TreeNode(5)
n3 =TreeNode(15)
n1.left = n2
n1.right = n3
n2.left = TreeNode(3)
n2.right = TreeNode(7)
n3.left = None
n3.right = TreeNode(18)
print(s.rangeSumBST(n1, 7, 15))
print(s.rangeSumBST2(n1, 7, 15))
print(s.rangeSumBST3(n1, 7, 15))