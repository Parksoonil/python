class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def printNode(self, l1: ListNode):
        if l1 is None:
            print("None")
        else:
            while l1:
                print(l1.val, end = "->")
                l1 = l1.next
            print()
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        odd = head
        even = head.next
        even_head = head.next
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
        odd.next = even_head
        return self.printNode(head)
list1 = ListNode(1)
list2 = ListNode(2)
list3 = ListNode(3)
list4 = ListNode(4)
list5 = ListNode(5)
list6 = ListNode(None)
list1.next = list2
list2.next = list3
list3.next = list4
list4.next = list5
list5.next = list6
a = Solution()
a.oddEvenList(list1)
list1 = ListNode(2)
list2 = ListNode(1)
list3 = ListNode(3)
list4 = ListNode(5)
list5 = ListNode(6)
list6 = ListNode(4)
list7 = ListNode(7)
list8 = ListNode(None)
list1.next = list2
list2.next = list3
list3.next = list4
list4.next = list5
list5.next = list6
list6.next = list7
list7.next = list8
a.oddEvenList(list1)