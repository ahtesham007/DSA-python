class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head, k):
        if not head or not k:
            return head

        cur = head
        count = 1
        # find len of list
        while cur.next:
            cur = cur.next
            count += 1

        # create loop
        cur.next = head

        # calculate end step to move
        k = count - (k % count)

        while k:
            cur = cur.next
            k-=1
        
        head = cur.next
        cur.next = None

        return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)


obj = Solution()
head = obj.rotateRight(head, 2)

while head:
    print(head.val)
    head = head.next

