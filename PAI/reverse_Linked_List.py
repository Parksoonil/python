class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
def reverseList(head: ListNode) -> ListNode:
    def reverse(node: ListNode, prev: ListNode = None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)
    return reverse(head)

def reverseList2(head: ListNode) -> ListNode:
    node, prev = head, None
    while node:
        next, node.next = node.next, prev
        prev, node = node, next
    return prev

if __name__ == "__main__":
    list1 = ListNode(1)
    list2 = ListNode(2)
    list3 = ListNode(3)
    list4 = ListNode(4)
    list5 = ListNode(5)
    l1 = list1
    list1.next = list2
    list2.next = list3
    list3.next = list4
    list4.next = list5
    print(reverseList(l1))
    print(reverseList2(l1))