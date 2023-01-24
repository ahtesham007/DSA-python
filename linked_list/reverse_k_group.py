class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head, k: int):
        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head

        cur = prev = nex = dummy
        count = 0

        # count length of linked-list

        while cur:
            cur = cur.next
            count += 1
        count -= 1
        while count >= k:
            cur = prev.next
            nex = cur.next

            for _ in range(1, k):
                cur.next = nex.next
                nex.next = prev.next
                prev.next = nex
                nex = cur.next

            prev = cur
            count -= k

        return dummy.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

obj = Solution()
head = obj.reverseKGroup(head, 2)

while head:
    print(head.val)
    head = head.next
