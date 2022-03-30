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
    def insertionSortList(self, head: ListNode) -> ListNode:
        cur = parent = ListNode(None)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            cur.next, head.next, head = head, cur.next, head.next
            cur = parent
        return cur.next
    def insertionSortList2(self, head: ListNode) -> ListNode:
        cur = parent = ListNode(0)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            cur.next, head.next, head = head, cur.next, head.next
            if head and cur.val > head.val:
                cur = parent
        return parent.next
s = Solution()
l = ListNode()
list1 = ListNode(4)
list2 = ListNode(2)
list3 = ListNode(1)
list4 = ListNode(3)
list1.next = list2
list2.next = list3
list3.next = list4
l.printNode(s.insertionSortList(list1))
list1 = ListNode(4)
list2 = ListNode(2)
list3 = ListNode(1)
list4 = ListNode(3)
list1.next = list2
list2.next = list3
list3.next = list4
l.printNode(s.insertionSortList2(list1))