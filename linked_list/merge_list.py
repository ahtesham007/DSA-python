class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):

        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.val > list2.val:
            list1, list2 = list2, list1
        head = list1
        while list1 and list2:
            temp = ListNode(None)
            while list1 and list1.val <= list2.val:
                temp = list1
                list1 = list1.next
            temp.next = list2
            list1, list2 = list2, list1
        
        return head

head = ListNode(1)

head.next = ListNode(3)

head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(4)

obj = Solution()
head = obj.mergeTwoLists(head, head2)

while head:
    print(head.val)
    head = head.next