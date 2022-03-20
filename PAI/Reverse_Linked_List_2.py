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
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m == n:
            return head
        root = start = ListNode(None)
        root.next = head
        for _ in range(m - 1):
            start = start.next
        end = start.next
        for _ in range(n - m):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return self.printNode(root.next)

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
a.reverseBetween(list1, 2, 4)