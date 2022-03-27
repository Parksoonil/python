import collections


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
    def invertTree(self, root:TreeNode) -> TreeNode:
        if root:
            root.left, root.right = \
                self.invertTree(root.right), self.invertTree(root.left)
            return root   
    def invertTree2(self, root:TreeNode) -> TreeNode:
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            if node:
                node.left, node. right = node.right, node.left

                queue.append(node.left)
                queue.append(node.right)
        return root
    def invertTree3(self, root:TreeNode) -> TreeNode:
        stack = collections.deque([root])
        while stack:
            node = stack.pop()
            if node:
                node.left, node. right = node.right, node.left

                stack.append(node.left)
                stack.append(node.right)
        return root
    def invertTree4(self, root:TreeNode) -> TreeNode:
        stack = collections.deque([root])
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.left)
                stack.append(node.right)
                node.left, node. right = node.right, node.left

        return root
s = Solution()
t = TreeNode()
n1 = TreeNode(4)
n2 = TreeNode(2)
n3 = TreeNode(7)
n4 = TreeNode(1)
n5 = TreeNode(3)
n6 = TreeNode(6)
n7 = TreeNode(9)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
t.printNode(s.invertTree(n1))
print()
n1 = TreeNode(4)
n2 = TreeNode(2)
n3 = TreeNode(7)
n4 = TreeNode(1)
n5 = TreeNode(3)
n6 = TreeNode(6)
n7 = TreeNode(9)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
t.printNode(s.invertTree2(n1))
print()
n1 = TreeNode(4)
n2 = TreeNode(2)
n3 = TreeNode(7)
n4 = TreeNode(1)
n5 = TreeNode(3)
n6 = TreeNode(6)
n7 = TreeNode(9)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
t.printNode(s.invertTree3(n1))
print()
n1 = TreeNode(4)
n2 = TreeNode(2)
n3 = TreeNode(7)
n4 = TreeNode(1)
n5 = TreeNode(3)
n6 = TreeNode(6)
n7 = TreeNode(9)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
t.printNode(s.invertTree4(n1))