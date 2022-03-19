
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = mergeTwoLists(l1.next, l2)
    while l1:
        print(l1.val, end = "->")
        l1 = l1.next

if __name__ == "__main__":
    list1 = ListNode(1)
    list2 = ListNode(2)
    list3 = ListNode(4)
    l1 = list1
    list1.next = list2
    list2.next = list3
    list1 = ListNode(1)
    list2 = ListNode(3)
    list3 = ListNode(4)
    l2 = list1
    list1.next = list2
    list2.next = list3
    mergeTwoLists(l1, l2)