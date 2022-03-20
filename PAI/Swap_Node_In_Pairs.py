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
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head

        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
        return self.printNode(head)

    def swapPairs2(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head

            prev.next = b

            head = head.next
            prev= prev.next.next
        return self.printNode(root.next)
    
    def swapPairs3(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            head.next = self.swapPairs3(p.next)
            p.next = head
            return self.printNode(p)
        return head

list1 = ListNode(1)
list2 = ListNode(2)
list3 = ListNode(3)
list4 = ListNode(4)
list1.next = list2
list2.next = list3
list3.next = list4
a = Solution()
a.swapPairs(list1)
list1 = ListNode(1)
list2 = ListNode(2)
list3 = ListNode(3)
list4 = ListNode(4)
list1.next = list2
list2.next = list3
list3.next = list4
a.swapPairs2(list1)
list1 = ListNode(1)
list2 = ListNode(2)
list3 = ListNode(3)
list4 = ListNode(4)
list1.next = list2
list2.next = list3
list3.next = list4
a.swapPairs3(list1)