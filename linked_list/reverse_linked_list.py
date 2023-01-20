from pyparsing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head):
        dummy = head
        prev = None

        while dummy:
            next_ele = dummy.next
            dummy.next = prev
            prev = dummy
            dummy = next_ele
        
        head = prev

        return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

obj = Solution()
head = obj.reverseList(head)


while head:
    print(head.val)
    head = head.next
