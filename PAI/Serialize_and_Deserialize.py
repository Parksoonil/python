import collections
import queue


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
    def serialize(self, root: TreeNode) -> str:
        queue = collections.deque([root])
        result = ["#"]
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)

                result.append(str(node.val))
            else:
                result.append("#")
        return ' '.join(result)
    def deserialize(self, data: str) -> TreeNode:
        if data == '# #':
            return None
        nodes = data.split()

        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])
        index = 2
        while queue:
            node = queue.popleft()
            if nodes[index] is not "#":
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1
            if nodes[index] is not "#":
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        return root
s = Solution()
t = TreeNode()
t1 = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(3)
n3 = TreeNode(4)
n4 = TreeNode(5)
t1.left = n1
t1.right = n2
n2.left = n3
n2.right = n4
print(s.serialize(t1))
t.printNode(s.deserialize(s.serialize(t1)))