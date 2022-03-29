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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            index = inorder.index(preorder.pop(0))

            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[0:index])
            node.right = self.buildTree(preorder, inorder[index + 1:])
            return node
s = Solution()
t = TreeNode()
t.printNode(s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))