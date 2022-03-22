import heapq
from pip import List

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def mergeKLists(lists: List[ListNode]) -> ListNode:
    root = result = ListNode(None)
    heap = []
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i, lists[i]))
    while heap:
        node = heapq.heappop(heap)
        idx = node[1]
        result.next = node[2]
        result = result.next
        if result.next:
            heapq.heappush(heap, (result.next.val, idx, result.next))
    return printNode(root.next)
def printNode(l1: ListNode):
    if l1 is None:
        print("None")
    else:
        while l1:
            print(l1.val, end = "->")
            l1 = l1.next
        print()
list1 = ListNode(1)
list2 = ListNode(2)
list3 = ListNode(5)
list1.next = list2
list2.next = list3
l1 = list1
list1 = ListNode(1)
list2 = ListNode(3)
list3 = ListNode(4)
list1.next = list2
list2.next = list3
l2 = list1
list1 = ListNode(2)
list2 = ListNode(6)
list1.next = list2
l3 = list1
print(mergeKLists([l1, l2, l3]))