class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head):

        if not head:
            return True
        dummy = head
        slow = fast = head

        # find middle
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse after middle
        slow.next = self.reverse(slow.next)

        slow = slow.next

        while slow:
            if dummy.val != slow.val:
                return False
            
            slow = slow.next
            dummy = dummy.next
        
        return True

    def reverse(self, temp_rev_pointer):
        temp_prev = None
        while temp_rev_pointer:
            temp_next = temp_rev_pointer.next
            temp_rev_pointer.next = temp_prev
            temp_prev = temp_rev_pointer
            temp_rev_pointer = temp_next
        return temp_prev

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)


obj = Solution()
print(obj.isPalindrome(head))