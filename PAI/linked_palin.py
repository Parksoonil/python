import collections
from typing import List
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None
def link_pal(head: ListNode) -> bool:
    q: List = []
    if not head:
        return True
    node = head

    while node is not None:
        q.append(node.val)
        node = node.next
    while len(q) > 1:
        if q.pop() != q.pop(0):
            return False
    return True

def link_pal2(head: ListNode) -> bool:
    q: collections.deque = collections.deque()
    
    if not head:
        return True
    node = head
    while node is not None:
        q.append(node.val)
        node = node.next
    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
    return True

def link_pal3(head: ListNode) -> bool:
    rev = None
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev
if __name__ == "__main__":
    list1 = ListNode(1)
    list2 = ListNode(2)
    list3 = ListNode(2)
    list4 = ListNode(1)
    head = list1
    list1.next = list2
    list2.next = list3
    list3.next = list4
    print(link_pal(head))
    print(link_pal2(head))
    print(link_pal3(head))
