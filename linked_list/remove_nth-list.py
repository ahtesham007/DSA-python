class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        start = ListNode(None)
        start.next = head
        fast = slow = start
        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return start.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

obj = Solution()
head = obj.removeNthFromEnd(head, 1)


while head:
    print(head.val)
    head = head.next
