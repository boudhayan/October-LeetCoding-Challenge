
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def length(self, root):
        k = 0
        while root is not None:
            k += 1
            root = root.next
        return k

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is not None:
            k = k % self.length(head)
        while k > 0:
            if head is None:
                return head
            current = head
            slast = None
            while current.next is not None:
                slast = current
                current = current.next
            if slast is None:
                return head
            else:
                newHead = slast.next
                newHead.next = head
                head = newHead
                slast.next = None
                k -= 1
        return head


def printList(root):
    while root is not None:
        print("{} -> ".format(root.val), end="")
        root = root.next
