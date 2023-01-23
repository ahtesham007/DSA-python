class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        result = ListNode()
        temp = result
        carry = 0

        while l1 or l2 or carry:
            curr_sum = 0
            if l1:
                curr_sum += l1.val
                l1 = l1.next
            
            if l2:
                curr_sum += l2.val
                l2 = l2.next
            curr_sum += carry
            carry = curr_sum // 10
            temp.next = ListNode(curr_sum%10)
            temp = temp.next
        
        return result.next
