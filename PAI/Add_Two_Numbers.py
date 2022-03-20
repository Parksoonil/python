from pip import List

class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head:ListNode) -> ListNode:
        node, prev = head, None
    
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev
    def toList(self, node: ListNode) -> List:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list
    def toReversedLinkedList(self, result: str) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node
    def printNode(self, l1: ListNode):
        if l1 is None:
            print("None")
            return
        else:
            while l1:
                print(l1.val, end = "->")
                l1 = l1.next
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))
        resultStr = int("".join(str(e) for e in a)) +\
                    int("".join(str(e) for e in b))
        return self.printNode(self.toReversedLinkedList(str(resultStr)))
list1 = ListNode(2)
list2 = ListNode(4)
list3 = ListNode(3)
list1.next = list2
list2.next = list3
l1 = list1
list1 = ListNode(5)
list2 = ListNode(6)
list3 = ListNode(4)
list1.next = list2
list2.next = list3
l2 = list1
a = Solution()
print(a.addTwoNumbers(l1, l2))

class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next
        return self.printNode(root.next)
    def printNode(self, l1: ListNode):
        if l1 is None:
            print("None")
            return
        else:
            while l1:
                print(l1.val, end = "->")
                l1 = l1.next

list1 = ListNode(2)
list2 = ListNode(4)
list3 = ListNode(3)
list1.next = list2
list2.next = list3
l1 = list1
list1 = ListNode(5)
list2 = ListNode(6)
list3 = ListNode(4)
list1.next = list2
list2.next = list3
l2 = list1
a = Solution2()
print(a.addTwoNumbers(l1, l2))