class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA, headB):
        a = headA
        b = headB

        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        
        return a