from pip import List

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    def printNode(self, node):
        if not node:
            return None
        if node.next:
            print(node.val, end = "->")
            self.printNode(node.next)
        else:
            print(node.val)
        
class Solution:
    def mergeTwoList(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoList(l1.next, l2)
        return l1 or l2
    def sortList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return self.mergeTwoList(l1, l2)
    def sortList2(self, head: ListNode) -> ListNode:
        p = head
        lst: List = []
        while p:
            lst.append(p.val)
            p =  p.next
        lst.sort()
        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next
        return head

            
s = Solution()
l = ListNode()
list1 = ListNode(4)
list2 = ListNode(2)
list3 = ListNode(1)
list4 = ListNode(3)
l1 = list1
list1.next = list2
list2.next = list3
list3.next = list4
l.printNode(s.sortList(l1))
list1 = ListNode(4)
list2 = ListNode(2)
list3 = ListNode(1)
list4 = ListNode(3)
l1 = list1
list1.next = list2
list2.next = list3
list3.next = list4
l.printNode(s.sortList2(l1))